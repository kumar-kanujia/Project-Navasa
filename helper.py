import os,shutil


def winsize():
    ''' To get the size of window in output as (columns, lines)'''
    oot=shutil.get_terminal_size()
    return oot.columns,oot.lines
    



# Funtion used to pause the system
def syspause():
    zz=input()



