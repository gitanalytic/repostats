import os

def getDepth(dirpath):
	index = dirpath.rfind('repo')
	count = dirpath[index:len(dirpath)].count('/')
	return count


def displayFiles():
	space = "   "
	for dirpath, dirs, files in os.walk(os.getcwd() + '/.data/repo'):
		current = dirpath[dirpath.rfind('/'):len(dirpath)]
		depth = getDepth(dirpath)
		print depth*space + current
		for filename in files:
			print space*(depth+1) + filename