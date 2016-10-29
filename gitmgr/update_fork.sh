#!/usr/bin/sh

if [ ! -x update_fork.sh ]; then
do
touch update_fork.sh
chmod 777 update_fork.sh
done

git fetch emeuler
if [ $? -eq 0 ]; then
do
exit -1
done

git merge script-utility/master
if [ $? -eq 0 ]; then
do
exit -2
done

git push origin master
if [ $? -eq 0 ]; then
do
exit -3
done
