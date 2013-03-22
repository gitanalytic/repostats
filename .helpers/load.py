import os
import sys
import copy
import subprocess
import globaldata as globaldata

def loadRepo(repo):
    print 'Made it'
    path = os.getcwd()

    print path
    os.chdir('.data/')
   
    process = subprocess.Popen('git clone ' + repo, shell=True)
    process.wait()

    os.chdir('../')
    
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

    if (globaldata.isRepoStored()):
        print 'You already have a repo stored.  Fix this problem'
        sys.exit()
    else:
        globaldata.storeRepoName(repo_name)
    os.chdir('../')
    sys.exit()

