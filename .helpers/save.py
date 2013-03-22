import os
import sys
import copy
import subprocess

import globaldata as globaldata

def saveRepo():
	path = os.getcwd()
	if globaldata.isRepoStored() is False:
		print 'shit' # Throw error!
	else:
		repoName = globaldata.getRepoName()
		process = subprocess.Popen('mv "' + path + '/.data/repo" "' + path + '/' + repoName + '"', shell=True).wait()