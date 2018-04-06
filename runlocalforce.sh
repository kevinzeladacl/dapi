#!/bin/bash
ps ax | grep "0.0.0.0:7799" | grep -v grep | awk '{print $1}' | xargs kill
clear
echo "......................................................................"
echo "By KevinZelada.cl"
echo "Run local server DAPI..."
nohup python3 manage.py runserver 0.0.0.0:7799 & 
echo "Restarting Django..."
sleep 10
echo "listo....ok"



 