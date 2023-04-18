1## a little thing to write a text file (or pdf) to document your practice ##
import os
import sys

author = ""

def create_journal():
    name = input("Name your journal: ") # name of the journal
    cwd = os.getcwd() # current working directory
    path = cwd + "/" + name # new directory (folder) path
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created!")
create_journal()

def open_journal():
    pass