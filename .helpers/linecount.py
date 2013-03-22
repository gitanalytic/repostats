import os
import sys
import copy
import subprocess
import mimetypes

def countLines():
    print os.getcwd()
    os.chdir('.data/repo')
    print os.getcwd()
    process = subprocess.Popen('ls', shell=True)

    sys.exit()

