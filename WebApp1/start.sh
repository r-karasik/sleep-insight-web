#!/bin/bash
# start the web server, to be run on AWS instance
cd ~/site || exit 2
echo Killing old server
if sudo killall -v gunicorn; then
    sleep 1
    sudo killall -9 -v gunicorn
    sleep 1
fi

mkdir -p ~/logs
logfile=~/logs/$(date +'%F-%H%M%S')
ln -fs $logfile.txt ~/log.txt
ln -fs $logfile-access.txt ~/access.txt

echo Starting new server
cd WebApp1
if ! sudo gunicorn -w 4 -b :80 -u ubuntu -g ubuntu --preload app:app \
    --daemon --error-logfile $logfile.txt --access-logfile $logfile-access.txt; then
    echo server failed to start
fi
sleep 2
if ! wget -nv -O /dev/null http://localhost; then
    cat $logfile.txt
    echo SERVER FAILED
    exit 1
fi
tail $logfile.txt
echo SERVER WORKS


