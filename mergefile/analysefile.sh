#!/usr/bin/sh
echo compare file $1 and $2
echo merge all the difference into $1
diff -c $1 $2 > test.dif
patch -p0 < test.dif
