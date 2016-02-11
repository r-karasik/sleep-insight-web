from flask import render_template, request, Markup, url_for
from app import app
import psycopg2
import psycopg2.extras
import json

app.jinja_env.filters['json'] = lambda v: Markup(json.dumps(v))
app.jinja_env.filters['unjson'] = lambda v: json.loads(v)

def connect_db():
    conn = psycopg2.connect(dbname='testdb')
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return conn, cur

@app.route('/')
@app.route('/index')
def index():    
    return render_template("index.html")

@app.route('/slides')
def slides():
    return render_template("slides.html")

@app.route('/allusers')
def allusers_page():
    db, cur = connect_db()
    cur.execute('SELECT child_id, description, summary_data FROM report_data ORDER BY child_id')
    results = cur.fetchall()
    return render_template("allusers.html", results=results)

@app.route('/user')
def user_page():
    db, cur = connect_db()
    cid_str = request.args.get('cid')

    try:
        cid = int(cid_str)
    except:
        cid = None

    results = []
    next_link = None
    if cid is not None:
        cur.execute("SELECT * FROM report_data WHERE child_id=%s", [cid])
        results = cur.fetchall()
        
        cur.execute("SELECT child_id FROM report_data WHERE child_id>%s ORDER BY child_id LIMIT 1",
                    [cid])
        next_results = cur.fetchall()
        if next_results:
            next_link = url_for('user_page', cid=next_results[0][0])
    
    return render_template("user.html", results=results, next_link=next_link)

@app.route('/users')
def users_page():
    db, cur = connect_db()
    try:
        cid = int(request.args.get('cid'))
    except:
        cid = 0

    try:
        count = int(request.args.get('count'))
        assert count >= 0
    except:
        count = 10

    cur.execute("SELECT * FROM report_data WHERE child_id>%s ORDER BY child_id LIMIT %s", 
                [cid, count + 1])
    results = cur.fetchall()
    next_link = None
    if len(results) > count:
        next_link = url_for('users_page', cid=results.pop()['child_id'], count=count)
    return render_template("user.html", 
                           results=results, 
                           next_link=next_link)

