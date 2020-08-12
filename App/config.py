import logging

""" LOGGING & LOGGERS """

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)
logger_format = '%(asctime)s-%(levelname)-5s-%(name)-8s :' \
                ' %(message)s'

debug_file_logger = logging.FileHandler(
    filename='logs/debug.log', encoding='utf8')
debug_file_logger.setLevel(logging.DEBUG)
debug_file_logger.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s >'
                                ' %(funcName)s >'
                                ' %(lineno)d}'))
logger.addHandler(debug_file_logger)

debug_stream_logger = logging.StreamHandler()
debug_stream_logger.setLevel(logging.INFO)
debug_stream_logger.setFormatter(logging.Formatter(
                                logger_format +
                                ' {%(filename)s > %(lineno)d}'))
logger.addHandler(debug_stream_logger)


# logging

logging.basicConfig('logs/debug.log', filemode='a')
