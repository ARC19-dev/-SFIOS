from config import *

test_logger = logging.getLogger('Test.Core')
tlogger = test_logger


# def extract_file_names(files):
#     filtered = list()
#     for file in files:
#         if file.split('.')[-1] == 'txt':
#             filtered += file
#     return filtered

# def get_files(path, hidden_folders = False, json = False, dictionary = False): # maybe add hidden_files
#     file_list = os.listdir(path)
#     all_files = list()
#     for entry in file_list:
#         full_path = os.path.join(path, entry)
#         if os.path.isdir(full_path):
#             if entry[0] != '.':
#                 all_files += get_files(full_path)
#         else:
#             all_files.append(full_path)
#     if json or dictionary:
#         # convert the list to a dict {'dirpath': 'filename'}
#         return list_to_dict(all_files)
#     else:
#         return all_files

# def list_to_dict(array):
#     dictionary = dict()
#     for item in array:
#         if 'win' in  OS:
#             value = item.split('\\')[-1]  # file name
#         else:
#             value = item.split('/')[-1]  # file name
#         key = item[:-len(value)]   # file path
#         dictionary[key] = value
#         print('key: ', key)
#         print('value: ', value)
#     return dictionary


# def get_files(path, hidden_folders = False):
#     files = list()
#     for (dirpath, dirname, filenames) in os.walk(path):
#         # print('dirpath: ', dirpath)
#         # print('dirname: ', dirname)
#         # print('filename: ', filenames)
#         for _dir in dirname:
#             if _dir[0] != '.':
#                 files += [os.path.join(dirpath, file)]
#         if dirname[0] != '.' and filenames[0] != '.': # fixme: maybe remove
#             files += [os.path.join(dirpath, file) for file in filenames]
#     return files

def extract(str, patter):
    pass

def search(lines, *, patters = PATTERNS):
    for line in lines():
        for pattern in patterns:
            match = re.search(pattern, line)
            return match.group(0)

'''

get_lines = search(get_lines)   or    @search
                                      def get_lines()

                    return obj = get_lines
'''

# @search
def get_lines(func):
    files = func()
    extracted = []
    if files is list():
        for file in files:
            with open(file, 'r') as File:
               extracted.append(File.readlines())
    else:
        for key, value in files:
            with open(value, 'r') as File:
               extracted.append(File.readlines())
    return extracted

# @get_lines
def get_files(path = input_value, hidden_folders = False, json = False, dictionary = False): # maybe add hidden_files
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


print('\n\n\n')
print('--------------- START ---------------')
# print(os.listdir('..'))
# print(extract_file_names(get_list_of_files('..')))
# print(get_files('..'))
# print(get_files('..'))
# print(list_to_dict(['C:/apps/fuck/test.txt', 'D:/video/help.mkv'])) # linux
# print(list_to_dict(['C:\\apps\\fuck\\test.txt', 'D:\\video\\help.mkv'])) # win
# print(get_files('..', json=True))
input_value = '..'
print(search())
files = [
    '..\\.gitignore', 
    '..\\App\\config.py', 
    '..\\App\\core.py', 
    '..\\App\\logs\\debug.log', 
    '..\\App\\main.py', 
    '..\\App\\test.py', 
    '..\\App\\__pycache__\\config.cpython-38.pyc', 
    '..\\datasets\\file-01.txt', 
    '..\\datasets\\file-02.txt', 
    '..\\datasets\\file-03.txt', 
    '..\\datasets\\pattern-detection.txt', 
    '..\\datasets\\todo-01.txt', 
    '..\\datasets\\todo-02.txt', 
    '..\\LICENSE', 
    '..\\README.md'
]




print('\n\n')

# os.uname()[0] or sys.platform

# def get_list_of_files(dir_name):
#     list_of_file = os.listdir(dir_name)
#     all_files = list()
#     for entry in list_of_file:
#         full_path = os.path.join(dir_name, entry)
#         if os.path.isdir(full_path):
#             all_files += get_list_of_files(full_path)
#         else:
#             all_files.append(full_path)
#     return all_files

# def extract_file_names(files):
#     filtered = list()
#     for file in files:
#         if file.split('.')[-1] == 'txt':
#             filtered += file
#     return filtered

# exract_files_names = get_list_of_files(exract_files_names)
# fillter = extract_file_names()



# todo: complete the search engine (or the search core)
# todo: don't enter folders starting with (.)
# todo: don't enter hidden folders (optional by user)
# todo: don't enter drive "C" except some special folders like documents or desktop etc.
# todo: indexing found files and folders (as aref saied)

# todo: open found files
# todo: search inside opened files
# todo: search for patterns
# todo: extract found pattern


# google: how to search fast in files using python
