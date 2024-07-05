#!/bin/sh

pip3 install -r requirements.txt
if [ ! -d logs ]; then
    mkdir logs
fi
if [ ! -d logs/package ]; then
    mkdir -p logs/package
fi
if [ ! -d logs/component_lib ]; then
    mkdir -p logs/component_lib
fi

_start=$(pgrep -f kessagent)
if [[ $_start == '' ]]; then
  brew services start kess-agent
fi

nohup python manage_evaluation.py product &

