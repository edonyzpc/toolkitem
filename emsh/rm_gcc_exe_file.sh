rm $(ls -la | grep '^-rwx.*' | sed 's/^-rwx.*[0-9] //g')
