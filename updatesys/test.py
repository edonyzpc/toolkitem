if __name__ == "__main__":
    import subprocess as sp
    pwd = open('./pwd.pyo')
    echo = ["echo"]
    tmp = pwd.readline().rstrip()
    print tmp
    echo.append(str(tmp))
    pwd.close()
    #echo.append(password)
    cmd = "sudo -S yum -y update"
    pipein = sp.Popen(echo, stdout=sp.PIPE)
    pipeout = sp.Popen(cmd.split(" "), stdin=pipein.stdout, stdout=sp.PIPE)

#p1 = sp.Popen(["dmesg"], stdout=sp.PIPE)
#p2 = sp.Popen(["grep", "hda"], stdin=p1.stdout, stdout=sp.PIPE)
#print p2.stdout.read()
