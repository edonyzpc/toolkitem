# -*- coding: utf-8 -*-
r"""
 #        .---.         .-----------
 #       /     \  __  /    ------
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    /
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /)
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'
 # ######################################################################################
 #
 # Author: edony - edonyzpc@gmail.com
 #
 # twitter : @edonyzpc
 #
 # Last modified: 2015-05-10 15:02
 #
 # Filename: filebuf.py
 #
 # Description: All Rights Are Reserved
 #
"""
class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = r"""
        STYLE: \033['display model';'foreground';'background'm
        DETAILS:
        FOREGROUND        BACKGOUND       COLOR
        ---------------------------------------
        30                40              black
        31                41              red
        32                42              green
        33                43              yellow
        34                44              blue
        35                45              purple
        36                46              cyan
        37                47              white
        DISPLAY MODEL    DETAILS
        -------------------------
        0                default
        1                highlight
        4                underline
        5                flicker
        7                reverse
        8                non-visiable
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;37;41m'
        self.tipcolor = '\033[0;31;42m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self,color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

class FileBuf(object):
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.file1_line_num = len(open(self.file1).readlines())
        self.file2_line_num = len(open(self.file2).readlines())
        self.buffer = []

    def mark_diff(self):
        f1 = open(self.file1)
        f2 = open(self.file2)
        if self.file1_line_num > self.file2_line_num:
            line1_num_counter = 0
            line2_num_counter = 0
            for line1 in f1.readlines():
                line2 = f2.readline()
                line1_num_counter += 1
                line2_num_counter += 1
                if line1 == line2:
                    continue
                else:
                    line1 = str(line1_num_counter) + '-' + line1
                    line2 = str(line2_num_counter) + '-' + line2
                    self.buffer.append(line1)
                    self.buffer.append(line2)
        else:
            line1_num_counter = 0
            line2_num_counter = 0
            for line2 in f2.readlines():
                line1 = f1.readline()
                line1_num_counter += 1
                line2_num_counter += 1
                if line1 == line2:
                    continue
                else:
                    line1 = str(line1_num_counter) + '+' + line1
                    line2 = str(line2_num_counter) + '+' + line2
                    self.buffer.append(line1)
                    self.buffer.append(line2)

    def write_file(self):
        file_write = open('tmp','w')
        for line in self.buffer:
            file_write.write(line)


if __name__ == '__main__':
    test_file_buf = FileBuf('f2.txt', 'f1.txt')
    test_file_buf.mark_diff()
    test_file_buf.write_file()
