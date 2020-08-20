import logging, sys, os, re, mimetypes

""" -------------------- LOGGING & LOGGERS -------------------- """

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
logger_format = '%(asctime)s-%(levelname)-5s-%(name)-8s :' \
                ' %(message)s'

debug_file_logger = logging.FileHandler(
    filename='logs/debug.log', encoding='utf8', mode='w')
debug_file_logger.setLevel(logging.DEBUG)
debug_file_logger.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s >'
                                ' %(funcName)s >'
                                ' %(lineno)d}'))
logger.addHandler(debug_file_logger)

debug_file_logger_1 = logging.FileHandler(
    filename='logs/debug.txt', encoding='utf8', mode='w')
debug_file_logger_1.setLevel(logging.DEBUG)
debug_file_logger_1.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s >'
                                ' %(funcName)s >'
                                ' %(lineno)d}'))
logger.addHandler(debug_file_logger_1)

debug_file_logger_2 = logging.FileHandler(
    filename='logs/info.txt', encoding='utf8', mode='w')
debug_file_logger_2.setLevel(logging.INFO)
debug_file_logger_2.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s >'
                                ' %(funcName)s >'
                                ' %(lineno)d}'))
logger.addHandler(debug_file_logger_2)

debug_stream_logger = logging.StreamHandler()
debug_stream_logger.setLevel(logging.INFO)
debug_stream_logger.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s > %(lineno)d}'))
logger.addHandler(debug_stream_logger)


# logging.basicConfig('logs/debug.log', filemode='a')

""" -------------------- File Extentions -------------------- """
# EXTENTIONS = [
#     'txt', 'todo', 'fixme', 'chert',
#     'py', 'html', 'php', 'js', 'jsx', 'ts', 'tsx'
#     ]

EXTENTIONS = ['txt', 'todo', 'log']

""" -------------------- OS DETECTION -------------------- """
OS = sys.platform


""" -------------------- PATTERNS -------------------- """
PATTERNS = [
    'todo:(.*)',
    'fixme:(.*)'
    ]
