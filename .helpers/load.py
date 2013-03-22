import os
import sys
import copy
import subprocess
import globaldata as globaldata

def loadRepo(repo):
    path = os.getcwd()

    os.chdir('.data/')
   
    process = subprocess.Popen('git clone ' + repo + ' &>> ../log.txt', shell=True)
    process.wait()

    os.chdir('../')
    
    index = repo.rfind('/')
    if (index == repo.__len__() - 1):
        repo = repo.rstrip('/')
        index = repo.rfind('/')
    repo_name = repo[index + 1:]
    os.chdir('.data')
    process = subprocess.Popen('mv ' + repo_name + '/ repo/', shell=True)
    process.wait()

    os.chdir('../')
    if (globaldata.isRepoStored()):
        print 'You already have a repo stored.  Fix this problem'
        sys.exit()
    else:
        globaldata.storeRepoName(repo_name)
    sys.exit()

