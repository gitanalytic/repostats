import fileextensions as fileextensions
import os

def getFileType(fileExtension):
	if fileExtension in fileextensions.everyFileExtension:
		return fileextensions.everyFileExtension[fileExtension]
	return False

def getLanguageFrequencies():
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