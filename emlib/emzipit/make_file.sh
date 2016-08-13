cc -c blowfish.c blowfish.h bf_locl.h
swig -python blowfish.i
cc -c `python2-config --cflags` blowfish.c  blowfish_wrap.c
cc -bundle `python2-config --ldflags` blowfish.o blowfish_wrap.o -o _blowfish.so
