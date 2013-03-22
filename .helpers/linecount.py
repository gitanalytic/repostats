import os
import sys
import copy
import subprocess
import mimetypes
import datastorage as datastorage

def countLines():
    if (not datastorage.repoIsStored()):
        print 'No repository is currently loaded.  Please load one and try again.'  
        print 'Type ./repostats --help for more information'
        sys.exit()
    os.chdir('.data/repo')

    total = 0

    for (path, dirs, files) in os.walk(os.getcwd()):
        if ('.git' in path):
            continue
        for filename in files:
            mime = mimetypes.guess_type(path+filename, False)
            if (mime[0] != None and mime[0].find('text') == 0):
                with open(path + '/' + filename) as f:
                    for i, l in enumerate(f):
                        pass
                total += i + 1
                
    print 'Number of lines in git repository: ' + str(total)
    os.chdir('../../')
    sys.exit()

