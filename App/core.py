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
# def SearchFile(path):
#     for dir_path, dir_names, file_names in os.walk(path):
#         for file_name in file_names:    
#                 if ext(file_name) in EXTENTIONS:
#                      with open(file_name, 'r') as file:
#                           a = file.readline()
#                           print(a)





def get_files(path,*, hidden_folders = False, json = False, dictionary = False): # maybe add hidden_files
    file_list = os.listdir(path)
    all_files = list()
    for entry in file_list:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            if entry[0] != '.':
                all_files += get_files(full_path)
        else:
            all_files.append(full_path)
    if json or dictionary:
        # convert the list to a dict {'dirpath': 'filename'}
        return list_to_dict(all_files)
    else:
        return all_files


def list_to_dict(array):
    dictionary = dict()
    for item in array:
        if 'win' in  OS:
            value = item.split('\\')[-1]  # file name
        else:
            value = item.split('/')[-1]  # file name
        key = item[:-len(value)]   # file path
        dictionary[key] = value
        print('key: ', key)
        print('value: ', value)
    return dictionary





