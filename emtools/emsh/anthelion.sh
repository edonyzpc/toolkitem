#!/bin/bash
# author:edony
picklefile="/home/edony/code/github/toolkitem/emtools/timstring.pickle"
if [ -f $picklefile ]; then
    rm $picklefile
fi
#chmod 777 /home/edony/code/github/toolkitem/emtools/login_sched.py
cd /home/edony/code/github/toolkitem/emtools/
python3 ./login_sched.py $1
#chmod 666 /home/edony/code/github/toolkitem/emtools/login_sched.py
