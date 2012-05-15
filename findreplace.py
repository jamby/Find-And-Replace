import os, fileinput, glob

# The function for replacing multiple items inside a dictionary
def replace_all(text, dic):
       for i, j in dic.iteritems():
             text = text.replace(i, j)
       return text

def checkFiles(filePath):
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
                checkFiles(currentFile)

# The dictionary needed for changing things
replaceDic = {"GameScene":"SceneOfThrones",
              "GameLayer":"LLLLAAAYYYEEERRRR",
              "void":"valid",
              "bool":"TRUEORFALSE",
              "int":"NUMBERSON"}


pathToSearch = './' # Our current directory and sub-directories that this Python file is in
scanDir(pathToSearch)
