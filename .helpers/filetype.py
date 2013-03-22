import fileextensions as fileextensions
import os
import sys
import datastorage as datastorage

def getFileType(fileExtension):
	if fileExtension in fileextensions.everyFileExtension:
		return fileextensions.everyFileExtension[fileExtension]
	return "File type not recognized"

def getLanguageFrequencies():
    if (not datastorage.repoIsStored()):
        print 'No repository is currently loaded.  Please load one and try again.'  
        print 'Type ./repostats --help for more information'
        sys.exit()

    frequencyMap = {}
    for root, dirs, files in os.walk(os.getcwd() + '/.data/repo'):
        if '.git' in root: continue
        for filename in files:
            index = filename.rfind('.')
            language = getFileType(filename[index:len(filename)])
            if(language): 
                if language in frequencyMap: frequencyMap[language]+=1
                else: frequencyMap[language] = 1
    return frequencyMap
