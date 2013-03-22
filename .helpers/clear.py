import os
import subprocess

import globaldata as globaldata

def clearRepo():
	path = os.getcwd()
	if globaldata.isRepoStored() is False:
		print 'There is no repo to clear.' 
	else:
		repoName = globaldata.getRepoName()
		process = subprocess.Popen('rm -rf "' + path + '/.data/repo"', shell=True).wait()
		globaldata.clearRepoName()