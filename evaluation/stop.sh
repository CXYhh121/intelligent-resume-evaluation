#!/bin/sh
pid=`ps aux | grep 'manage_evaluation.py' | grep -v grep  | awk '{print$2}'`
if [ ! -z "${pid}" ]; then
    kill ${pid}
fi
_start=$(pgrep -f kessagent)
if [[ $_start != '' ]]; then
  brew services stop kess-agent
fi
