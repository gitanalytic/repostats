#!/usr/bin/python
import os
import sys
import copy
import subprocess

real_path = os.path.realpath(__file__)
os.chdir(real_path[:real_path.rfind('/')])

sys.path.insert(0, os.path.abspath(os.getcwd() + '/.helpers'))

import filetype as filetype
import linecount as linecount
import manual as manual
import datastorage as data
import showfiles as showfiles

import getopt
keywords = ['load=','ls','file=', 'save', 'lang', 'clear', 'linecount', 'help']
try:
    opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
except getopt.GetoptError, err:
    print 'Error: ' + str(err)
    manual.printHelp()
    sys.exit(2)

if (opts.__len__() == 0 or opts.__len__() > 2):
    manual.printHelp()
    sys.exit()
for o,p in opts:
    if o == '--load':
        data.loadRepo(p)
    elif o == '--ls':
        showfiles.displayFiles()
        #list files
    elif o == '--file':
        x = 0
        filename = p
        index = filename.rfind('.')
        language = filetype.getFileType(filename[index:len(filename)])
        print language
        #do file analytics
    elif o == '--save':
        data.saveRepo()
    elif o == '--lang':
        x = 0
        languages = filetype.getLanguageFrequencies()
        print ' '
        for language in languages:
            message = language + " : " + str(languages[language]) + " file"
            if languages[language] > 1: message += "s"
            print message
        print ' ' 
    elif o == '--clear':
        data.clearRepo()
    elif o == '--linecount':
        linecount.countLines()
    elif o == '--help':
        manual.printHelp()
