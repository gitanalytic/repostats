import os

def isRepoStored():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		line = repoNameFile.readline()
		line = line[1:]

		if len(line) == 0:
			return False
		else:
			return True

	return False

def clearRepoName():
	storeRepoName('')

def storeRepoName(repoName):
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r+') as repoNameFile:
		repoNameFile.seek(0)
		repoNameFile.write(repoName)
		repoNameFile.truncate()

def getRepoName():
	path = os.getcwd()
	with open(path + '/.helpers/global.txt', 'r') as repoNameFile:
		return repoNameFile.readline()


# Example Usage:

# globaldata.clearRepoName()
# if globaldata.isRepoStored() is False:
#     print 'yay'
# globaldata.storeRepoName('test')
# if globaldata.isRepoStored() is True:
#     print globaldata.getRepoName()