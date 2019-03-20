#!/bin/bash
nohup python3 ./manage.py runserver 0.0.0.0:8001 >> ../logs/request.log &
echo "启动成功"
