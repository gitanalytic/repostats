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
import filetype as filetype
import linecount as linecount
import datastorage as data
import showfiles as showfiles

import getopt
keywords = ['load=','ls','file=', 'save', 'lang', 'clear', 'linecount']
opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
fileMode = False
filename = ""
for o,p in opts:
    if o in ('-n','--load'):
        data.loadRepo(p)
    elif o in ('-l','--ls'):
        x = 0
        showfiles.displayFiles()
        #list files
    elif o in ('-f', '--file'):
        x = 0
        fileMode = True
        filename = p
        #do file analytics
    elif o in ('-s', '--save'):
        data.saveRepo()
    elif o == '--lang':
        x = 0
        if fileMode:
            index = filename.rfind('.')
            language = filetype.getFileType(filename[index:len(filename)])
            if(language): print language
        else:
            languages = filetype.getLanguageFrequencies()
            for language in languages:
                message = language + " : " + str(languages[language]) + " file"
                if languages[language] > 1: message += "s"
                print message
        #print langs
    elif o == '--clear':
        data.clearRepo()
    elif o == '--linecount':
        linecount.countLines()
