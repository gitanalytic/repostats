import os
import sys
import copy
import subprocess

def saveRepo():
	path = os.getcwd()
	print 'mv ' + path + '/.data/repo ' + path + '/'
	process = subprocess.Popen('mv "' + path + '/.data/repo" "' + path + '/"', shell=True).wait()