#!/usr/bin/python
import os
import sys
import copy
import subprocess

real_path = os.path.realpath(__file__)
os.chdir(real_path[:real_path.rfind('/')])

sys.path.insert(0, os.path.abspath(os.getcwd() + '/.helpers'))

import load as load
import save as save
import clear as clear
import globaldata as globaldata
import fileextensions as fileextensions

keywords = ['load=','ls','file=', 'save', 'lang', 'clear']
import getopt
opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
fileMode = False
filename = ""
for o,p in opts:
    if o in ('-n','--load'):
        load.loadRepo(p)
    elif o in ('-l','--ls'):
        x = 0
        #list files
    elif o in ('-f', '--file'):
        x = 0
        fileMode = True
        filename = p
        #do file analytics
    elif o in ('-s', '--save'):
        save.saveRepo()
    elif o == '--lang':
        x = 0
        if fileMode:
            index = filename.rfind('.')
            language = fileextensions.getFileType(filename[index:len(filename)])
            if(language): print language
        else:
            for root, dirs, files in os.walk(os.getcwd() + '/.data/repo'):
                files = files[2:-2]
                index = files.rfind('.')
                language = fileextensions.getFileType(files[index:len(filename)])
                if(language): print language
        #print langs
    elif o == '--clear':
        x = 0
        #clear
