# IN THE NAME OF GOD
from config import *

""" -------------------- LOGGER -------------------- """
core_logger = logging.getLogger('Core')
cl = core_logger


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



def search(lines, *, patters = PATTERNS):
    for line in lines:
        for pattern in patterns:
            match = re.search(pattern, line)
            return match.group(0)


def get_lines(files):
    cl.debug(type(files))
    extracted = []
    if type(files) is list:
        cl.debug('list detected')
        for file in files:
            with open(file, 'r') as File:
               extracted.append(File.readlines())
    else:
        cl.debug('dict detected')
        for key, value in files.items():
            with open(value, 'r') as File:
               extracted.append(File.readlines())
    return extracted


def get_files(path: str,*, hidden_folders = False, json = False, dictionary = False): # maybe add hidden_files
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


def main():
    cl.info('----- STARTING -----')
    cl.debug('Debugging started')
    search(get_lines(get_files('.')))

if __name__ == '__main__':
    main()