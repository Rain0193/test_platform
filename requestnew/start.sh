#!/bin/bash
nohup python3 ./requestnew/manage.py runserver 0.0.0.0:8000 >> ../logs/request.log &
echo "启动成功"
