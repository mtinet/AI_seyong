#!/bin/sh



proc=`ps -ef |grep python |grep "smartM_ai_server.py" |awk '{print$2}'`

if [ X"$proc" != X"" ]; then
	echo "[$proc] aleady executed.."
else
	sudo env "PATH=$PATH" nohup python smartM_ai_server.py   output.log 2&1
fi


