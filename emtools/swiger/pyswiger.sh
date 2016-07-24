#!/bin/sh
# -*- encoding:utf-8 -*-

if [ $# -lt 1 ];then
    echo "Please check your swig interface file"
    exit -1
elif [ $(uname) == "Darwin" -o $(uname) == "darwin" ];then
    interface=$1
    suffix=${interface#*.}
    name=${interface%.*}
    if [ "$suffix" == "i" -o "$suffix" == "swg" ];then
        swig -python $interface
        cc -c `python-config --cflags` $name".c" $name"_wrap.c"
        cc -bundle `python-config --ldflags` $name".o" $name"_wrap.o" -o "_"$name".so"
    fi
    exit 0
elif [ $(uname) == "Linux" -o $(uname) == "linux" ];then
    interface=$1
    suffix=${interface#*.}
    name=${interface%.*}
    if [ "$suffix" == "i" -o "$suffix" == "swg" ];then
        swig -python $interface
        gcc -c `python-config --cflags` $name".c" $name"_wrap.c"
        ld -shared $name".o" $name"_wrap.o" -o "_"$name".so"
    fi
    exit 0
fi
#swig -python example.i
#cc -c `python2-config --cflags` example.c example_wrap.c
#cc -bundle `python2-config --ldflags` example.o example_wrap.o -o _example.so
