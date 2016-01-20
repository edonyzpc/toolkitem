#!/bin/bash
# author:edony
linuxpicklefile="/home/edony/code/github/toolkitem/emtools/timstring.pickle"
macpicklefile="/Users/edony/coding/toolkitem/emtools/timstring.pickle"
mac="Darwin"
linux="Linux"
if [ $mac = $(uname -s) ]; then
    echo "Darwin"
    if [ -f $macpicklefile ]; then
        rm $macpicklefile
    fi
    cd /Users/edony/coding/toolkitem/emtools/
    python3 ./login_sched.py $1
elif [ $linux = $(uname -s) ]; then
    echo "Linux"
    if [ -f $linuxpicklefile ]; then
        rm $linuxpicklefile
    fi
    cd /home/edony/code/github/toolkitem/emtools/
    python3 ./login_sched.py $1
fi
#chmod 777 /home/edony/code/github/toolkitem/emtools/login_sched.py
#cd /home/edony/code/github/toolkitem/emtools/
#python3 ./login_sched.py $1
#chmod 666 /home/edony/code/github/toolkitem/emtools/login_sched.py
