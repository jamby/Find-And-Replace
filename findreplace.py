import os, fileinput, glob, sys

# The function for replacing multiple items inside a dictionary
def replace_all(text, dic):
       for i, j in dic.iteritems():
             text = text.replace(i, j)
       return text

def checkFile(filePath):
       # The various files we need
       fileToSearch = filePath
       oldFileName  = fileToSearch + '.old'
       tempFileName = fileToSearch + '.temp'
       fileOut = open(tempFileName, 'w')
       # For every line, replace the corresponding words with the dictionary
       for line in fileinput.input(fileToSearch):
              newLine = replace_all(line, replaceDic)
              fileOut.write(newLine)
       fileOut.close()
       # Rename the original file to something else so we can overwrite it
       os.rename(fileToSearch, oldFileName)
       # Rename the temp file to the original
       os.rename(tempFileName, fileToSearch)
       # Remove the old file name, because we don't need it
       os.remove(oldFileName)

def scanDir(path):
    for currentFile in glob.glob(os.path.join(path, '*')):
        if not currentFile.endswith('.py'): # If it's not a python file
            if os.path.isdir(currentFile): # If it's a directory, recursion!
                scanDir(currentFile)
            if not os.path.isdir(currentFile): # If it's not a directory, check the files!
                   if os.access(currentFile, os.W_OK) == True:
                          checkFile(currentFile)

numPhrases = int(raw_input("How many phrases are being changed? ")) # Asking the user how many keys and value pairs there are

if(numPhrases == '' or numPhrases == 0):  # If there are 0 phrases wanted or nothing written
       sys.exit()                         # Exit from the script

i = 0
while(i < numPhrases):
       word1 = raw_input("What is the phrase you're looking for? ") 
       word2 = raw_input("What are you replacing it with? ")
       if(i == 0): # If this is the first word, must make the variable a dictionary
              replaceDic = {word1:word2}
       else: # Otherwise, just update the dictionary
              replaceDic.update({word1:word2})
       i += 1

pathToSearch = raw_input("File to search in (nothing to search all of the files and directories): ")

if(pathToSearch == ''):
    scanDir('./') # Our current directory and sub-directories that this Python file is in
else:
    checkFile(pathToSearch)

raw_input("\n\nPress Enter to exit...") # Here to make sure the script is finished
