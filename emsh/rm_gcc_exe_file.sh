rmlist=$(ls -la | grep '^-rwxrwxr-x.*' | sed 's/^-rwx.*[0-9] //g')
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
