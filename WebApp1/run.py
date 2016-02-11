#!/usr/bin/env python
from gevent.wsgi import WSGIServer
from app import app
app.run(debug = True, host = '0.0.0.0')

#http_server = WSGIServer(('', 5000), app)
#print 'ready at http://localhost:5000/'
#http_server.serve_forever()
