#!/usr/bin/sh
# Description
echo compare file $1 and $2
echo merge all the difference into $1
# Mark up difference of two files
diff -c $1 $2 > buf.diff
# Remove the delete lines
#sed -i 's/^-\( \{1,\}.*\)/ /2' buf.diff
sed -i 's/^-\( \{1,\}.*\)/ \1/g' buf.diff
sed -i 's/^!\( \{1,\}.*\)/ \1/g' buf.diff
#grep '^- \{1,\}' buf.diff | sed 's/^-/ /'
VAR=$(grep '^- \{1,\}' buf.diff | sed 's/^-/ /')
NUM=$(echo "$VAR" | wc -l)
OPT=1
#sed -i 's/^- \{1,\}.*/@@@@/' buf.diff    # marker for patch file
if [ "$NUM" -eq "$OPT" ];then
    echo only one line
#    sed -i "s/^@@@@/${VAR}/" buf.diff
    patch $1 buf.diff
elif [ "$NUM" -gt "$OPT" ];then
    echo multiple lines
#    sed -i "s/^@@@@/${VAR}/1" buf.diff
#    sed -i 's/@@@@/d' buf.diff
    patch $1 buf.diff
fi
#rm -f buf.diff
