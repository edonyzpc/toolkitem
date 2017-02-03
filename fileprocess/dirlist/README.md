Project Directory List

## Goal

Start from the root directory that is given by the caller and crawl the directory recursivley whcih will be record into the database.
- [ ] list the directory recursively and get all directories including all subdirectory
- [ ] speed up the list with multiprocess
- [ ] sequence the dirlist class with pickle

## Architecture

* Builtin module `os` has the method to list the directory `os.listdir(root_path)`

* Builtin module `os` has the method to check if it is directory `os.path.isdir(mem)`

* Builtin module `multiprocess` hash the methods to create a process pool executing some operation

* A proper scanning method to walk through all of the sub-directories `DFS`

* ADT for engieering purpose

![dirlist node](https://github.com/edonyM/toolkitem/blob/master/fileprocess/dirlist/dir_node.png)

## API

* DFS algorithm scan the directory

* Data Abstract Type of directory

## Descriptions

## Other

