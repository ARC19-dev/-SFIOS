from config import *

test_logger = logging.getLogger('Test.Core')
tlogger = test_logger

# tlogger.debug('This is a debug msg') 
# tlogger.info('This is a info msg') 
# tlogger.warning('This is a warning msg') 
# tlogger.error('This is a error msg') 
# tlogger.critical('This is a critical msg') 

# logger.debug('This is a debug msg') # 10
# logger.info('This is a info msg') # 20
# logger.warning('This is a warning msg') # 30
# logger.error('This is a error msg') # 40
# logger.critical('This is a critical msg') # 50

# print('logged successfully')

# loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
# print(loggers)
# print(sys.platform)

def extract_file_names(files):
    filtered = list()
    for file in files:
        if file.split('.')[-1] == 'txt':
            filtered += file
    return filtered

def get_list_of_files(dir_name):
    list_of_file = os.listdir(dir_name)
    all_files = list()
    for entry in list_of_file:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files += get_list_of_files(full_path)
        else:
            all_files.append(full_path)
    return all_files

print('\n\n\n')
print('--------------- START ---------------')
# print(os.listdir('..'))
print(extract_file_names(get_list_of_files('..')))




# todo: solve the problem of the logging (logger logs two times)
# todo: start the search engine (or the search core)
