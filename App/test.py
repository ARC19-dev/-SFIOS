from config import *

test_logger = logging.getLogger('Test.Core')
tlogger = test_logger

tlogger.debug('This is a debug msg') 
tlogger.info('This is a info msg') 
tlogger.warning('This is a warning msg') 
tlogger.error('This is a error msg') 
tlogger.critical('This is a critical msg') 

# logger.debug('This is a debug msg') # 10
# logger.info('This is a info msg') # 20
# logger.warning('This is a warning msg') # 30
# logger.error('This is a error msg') # 40
# logger.critical('This is a critical msg') # 50
                                                            

print('logged successfully')

loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
print(loggers)


# todo: solve the problem of the logging (logger logs two times)
# todo: start the search engine (or the search core)



