import os

def dfs_myDir(path, printDir = None, printFile = None):
    stack = []
    ret = []
    stack.append(path)
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
            if printDir:
                printDir(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            if printFile:
                printFile(tmp)
    return ret

def printDir(path):
    print "dir: " + path

def printFile(path):
    print "file: " + path

d = dfs_myDir(r'../', printDir, printFile)
