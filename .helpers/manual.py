import os
import sys
import copy
import subprocess

def printHelp():
    print ' '
    print 'Usage:'
    print ' '
    print '  --load url   : Temporarily loads github repository located at url. url can be in one of three' 
    print '                 forms: https://github.com/REPOSITORY, github.com/REPOSITORY, or REPOSITORY where' 
    print '                 REPOSITORY is username/repositoryname (for example "zsaraf/opensourcery)'
    print ' '
    print '  --ls         : Lists all directories in a heirarchical, depth first format.  Lists all sub-files' 
    print '                 and sub-directories recursively before moving on to the next directory'
    print ' '
    print '  --file name  : Given a file name, prints the language the file is written, based on the extension' 
    print '                 (for example, homepage.js is a Javascript file'
    print ' '
    print '  --save       : Permanently loads the already loaded github repository into the repostat directory.'
    print '                 You can now move this wherever you please'
    print ' '
    print '  --lang       : Prints to the console all of the languages used in the repository and their frequencies.'  
    print '                 Determines the language of each file using the file extension'
    print ' '
    print '  --clear      : Clears and removes the github repository currently loaded.  Clearing will remove this' 
    print '                 repository from your memory.'
    print ' '
    print '  --linecount  : Calculates the number of lines in the entire repository (anything beginning with the' 
    print '                 text/ identifier, so no executables, images, etc.)'
    print ' '
