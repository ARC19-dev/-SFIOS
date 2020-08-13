# IN THE NAME OF GOD
from config import *


""" -------------------- FUNCTIONS -------------------- """
def ext(file_name):
    return file_name.split('.')[-1]


""" -------------------- PROCCESS -------------------- """
# get OS

# common functions ( linux = win )


# for linux 
    # get the list of directory and files
    # filter the files if they are binary
    # filter the files by extentions (.txt, .py, .html, ...) ( remove for example .png )
    # create a final list of filtered files
    # open files one by one and search inside them ( mine them :) )
    # show the result


# for windows
    # get the list of directory and files
    # filter the files if they are binary
    # filter the files by extentions (.txt, .py, .html, ...) ( remove for example .png )
    # create a final list of filtered files
    # open files one by one and search inside them ( mine them :) )
    # show the result


# Search file in linux and windowns
def SearchFile(path):
    for dir_path, dir_names, file_names in os.walk(path):
        for file_name in file_names:    
                if ext(file_name) in EXTENTIONS:
                     with open(file_name, 'r') as file:
                          a = file.readline()
                          print(a)

path = 'G:\\projects\\Python\\ReDeeps\\datasets'
SearchFile(path)



# extention = lambda file_name : file_name.split('.')[-1]