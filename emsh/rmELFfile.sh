sys=$(uname)
sys_m="Darwin"
sys_l="Linux"
if [ "$sys" == "$sys_l" ]
then
    if [ ! -n "$1" ]
    then
        rmlist=$(ls -la | grep '^-rwxrwxr-x.*' | sed 's/^-rwxrwxr-x.*[0-9] //g')
    else
        rmlist=$(ls -la $1| grep '^-rwxrwxr-x.*' | sed 's/^-rwxrwxr-x.*[0-9] //g')
    fi
fi
if [ "$sys" == "$sys_m" ]
then
    if [ ! -n "$1" ]
    then
        rmlist=$(ls -la | grep '^-rwxr-xr-x.*' | sed 's/^-rwxr-xr-x.*[0-9] //g')
    else
        rmlist=$(ls -la $1| grep '^-rwxr-xr-x.*' | sed 's/^-rwxr-xr-x.*[0-9] //g')
    fi
fi
echo $rmlist
echo "Remove?"
read check
yes="y"
if [ "$check" == "$yes" ]
then
    if [ ! -n "$rmlist" ]
    then
        echo "No Need to Remove"
    else
        rm $rmlist
    fi
else
    echo "No Remove"
fi
