import os
import sys
import copy
import subprocess

def loadRepo(repo):
    print 'Made it'
    path = os.getcwd()

    print path
    os.chdir('.data/')
    process = subprocess.Popen('ls -alrth', shell=True)
    process.wait()
   
    process = subprocess.Popen('git clone ' + repo, shell=True)
    process.wait()

    os.chdir('../')
