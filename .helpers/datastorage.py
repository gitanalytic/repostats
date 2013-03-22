import os
import subprocess

import globaldata as globaldata

# repoIsStored checks if the .helpers/global.txt contains a repo name
def repoIsStored():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		line = repoNameFile.readline()
		line = line[1:]

		if len(line) == 0:
			return False
		else:
			return True

	return False

# clearRepoNames clears the .helpers/global.txt file
def clearRepoName():
	storeRepoName('')

# storeRepoName stores a repo name in .helpers.global.txt files
def storeRepoName(repoName):
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r+') as repoNameFile:
		repoNameFile.seek(0)
		repoNameFile.write(repoName)
		repoNameFile.truncate()

# returns the name of the repo in the .helpers/global.txt file
def getRepoName():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		return repoNameFile.readline()

# saveRepo moves the repo from .data to the repostats directory and clears the repo name in .helpers/global.txt
def saveRepo():
	path = os.getcwd()
	if repoIsStored() is False:
		print 'There is no repo to be saved' 
	else:
		repoName = getRepoName()
		process = subprocess.Popen('mv "' + path + '/.data/repo" "' + path + '/' + repoName + '"', shell=True).wait()
		clearRepoName()

# clearRepo clears in .data and the repo name in .helpers/global.txt
def clearRepo():
	path = os.getcwd()
	if repoIsStored() is False:
		print 'There is no repo to clear.' 
	else:
		repoName = getRepoName()
		process = subprocess.Popen('rm -rf "' + path + '/.data/repo"', shell=True).wait()
		clearRepoName()

# loadRepo takes a github url and loads and saves the repo to the .data directory
def loadRepo(repo):
    path = os.getcwd()

    os.chdir('.data/')
   
    process = subprocess.Popen('git clone ' + repo + ' >> ../log.txt', shell=True).wait()

    
    index = repo.rfind('/')
    if (index == repo.__len__() - 1):
        repo = repo.rstrip('/')
        index = repo.rfind('/')
    repo_name = repo[index + 1:]
    process = subprocess.Popen('mv ' + repo_name + '/ repo/', shell=True).wait()

    os.chdir('../')
    if (repoIsStored()):
        print 'You already have a repo stored.  Fix this problem'
        sys.exit()
    else:
        storeRepoName(repo_name)