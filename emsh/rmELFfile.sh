if [ ! -n "$1" ]
then
    rmlist=$(ls -la | grep '^-rwxrwxr-x.*' | sed 's/^-rwxrwxr-x.*[0-9] //g')
else
    rmlist=$(ls -la $1| grep '^-rwxrwxr-x.*' | sed 's/^-rwxrwxr-x.*[0-9] //g')
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
