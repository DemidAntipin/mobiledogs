import socket
from logging.handlers import TimedRotatingFileHandler
import hashlib
import logging
import sys

ip_address = socket.gethostbyname(socket.gethostname())

FORMATTER_STRING = "%(asctime)s — %(name)s — %(levelname)s — %(message)s - IP: {}".format(hashlib.md5(ip_address.encode('utf-8')).hexdigest())

FORMATTER = logging.Formatter(FORMATTER_STRING)
LOG_FILE = "../logs/logger.log"

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    logger.addHandler(console_handler)

    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(FORMATTER)
    logger.addHandler(file_handler)

    return logger
