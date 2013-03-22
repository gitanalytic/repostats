#!/usr/bin/python
import os
import sys
import copy
import subprocess


file = os.getcwd()
print 'CWD: ' + file
for dirname,dirnames, filenames in os.walk('.'):
    print dirname
process = subprocess.Popen('ls -alrth .', shell=True)
process.wait()
sys.exit()



keywords = ['load=','ls','file=', 'save', 'lang', 'clear']
import getopt
opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
for o,p in opts:
    if o in ('-n','--load'):
        process = subprocess.Popen('mkdir ~/Code/CS184/gitanalytic/repostats/repository/', shell=True)
        process.wait()
        process = subprocess.Popen('git clone https://github.com/zsaraf/Viral/', shell=True)
        process.wait()
        process = subprocess.Popen('mv ./Viral ./repository')
        process.wait()
    elif o in ('-l','--ls'):
        x = 0
        #list files
    elif o in ('-f', '--file'):
        x = 0
        #do file analytics
    elif o in ('-s', '--save'):
        x = 0
        #save repository
    elif o is '--lang':
        x = 0
        #print langs
    elif o is '--clear':
        x = 0
        #clear
        
f = open(encoded_file, 'r')
not_found = True
encoded_line = ''
