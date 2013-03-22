#!/usr/bin/python
import os
import sys
import copy
import subprocess

file = ''
encoded_file = '/home/zach/Code/CMessAround/ImportantInfo'

keywords = ['password=','ls']
import getopt
opts, remainder = getopt.getopt(sys.argv[1:],'p:l',keywords)
for o,p in opts:
    if o in ('-n','--load'):
        #load new file
    elif o in ('-l','--ls'):
        #list files
    elif o in ('-f', '--file'):
        #do file analytics
    elif o in ('-s', '--save'):
        #save repository
    elif o is '--lang':
        #print langs
    elif o is '--clear':
        #clear
        
f = open(encoded_file, 'r')
not_found = True
encoded_line = ''
