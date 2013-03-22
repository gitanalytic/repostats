import os
import sys
import datastorage as datastorage

def getDepth(dirpath):
	index = dirpath.rfind('repo')
	count = dirpath[index:len(dirpath)].count('/')
	return count


def displayFiles():
    if (not datastorage.repoIsStored()):
        print 'No repository is currently loaded.  Please load one and try again.'  
        print 'Type ./repostats --help for more information'
        sys.exit()
    space = "   "
    for dirpath, dirs, files in os.walk(os.getcwd() + '/.data/repo'):
	    current = dirpath[dirpath.rfind('/'):len(dirpath)]
	    depth = getDepth(dirpath)
	    print depth*space + current
	    for filename in files:
		    print space*(depth+1) + filename
