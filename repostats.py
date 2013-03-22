#!/usr/bin/python
import os
import sys
import copy
import subprocess

sys.path.insert(0, os.path.abspath(os.getcwd() + '/.helpers'))

import load as load
import save as save
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
        
        index = p.rfind('/')
        if (index == p.__len__() - 1):
            p = p.rstrip('/')
            index = p.rfind('/')
        repo_name = p[index + 1:]
        print repo_name
        print os.getcwd()
        os.chdir('.data')
        process = subprocess.Popen('mv ' + repo_name + '/ repo/', shell=True)
        process.wait()
        os.chdir('../')
        sys.exit()
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
            print 'here'
            for root, dirs, files in os.walk(os.getcwd() + '/.data'):
                #index = filename.rfind('.')
                print files
                # language = fileextensions.getFileType(filename[index:len(filename)])
                # if(language): print language
        #print langs
    elif o == '--clear':
        x = 0
        #clear
