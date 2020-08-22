# IN THE NAME OF GOD
from config import *

""" -------------------- LOGGER -------------------- """
core_logger = logging.getLogger('Core')
cl = core_logger


""" -------------------- FUNCTIONS -------------------- """


def ext(file_name):
    return file_name.split('.')[-1]


textchars = bytearray({7, 8, 9, 10, 12, 13, 27} |
                      set(range(0x20, 0x100)) - {0x7f})


def is_binary_string(bytes): return bool(bytes.translate(None, textchars))


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

# def search(lines, *, patterns=PATTERNS):
# matches = []
# count = 0
# for line in lines:
# if count >= 5:
# return matches
# for pattern in patterns:
# match = re.split(pattern, line)
# match = re.search(pattern, str(line))
# if match:
# matches.append(match.group(0))
# count += 1
# return matches

# fight
def search(files, patterns=PATTERNS):
    matches = []
    for file in files:
        for line in file:
            for ptr in patterns:
                match = re.findall(ptr, line)
                if match:
                    matches.append(match)
    return matches


def get_lines(files):
    # cl.debug('FILES: %s' % files)
    # cl.debug(type(files))
    extracted = []
    if type(files) is list:
        cl.debug('list detected')
        for file in files:
            with open(file, 'r', encoding="utf8") as File:
                extracted.append(File.readlines())
    else:
        cl.debug('dict detected')
        for value in files.values():
            with open(value, 'r', encoding="utf8") as File:
                extracted.append(File.readlines())
    return extracted


def get_files(path: str, *, hidden_folders=False, json=False, dictionary=False):  # maybe add hidden_files
    cl.debug('get_files(%s)' % path)
    file_list = os.listdir(path)
    all_files = list()
    for entry in file_list:
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            if entry[0] != '.':
                all_files += get_files(full_path)
        else:
            with open(full_path, 'rb') as f:
                if (is_binary_string(f.read(128))):
                    cl.debug('Binary file:  %s' % full_path)
                else:
                    all_files.append(full_path)
    # convert the list to a dict {'dirpath': 'filename'}
    if json or dictionary:
        cl.debug(all_files)
        return list_to_dict(all_files)
    else:
        cl.debug(all_files)
        return all_files


def list_to_dict(array):
    dictionary = dict()
    for item in array:
        if 'win' in OS:
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
    lines = get_lines(get_files('..\\datasets'))
    m = search(lines)
    cl.info(m)


if __name__ == '__main__':
    main()
