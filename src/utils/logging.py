import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_INFO_LOG = os.path.join(BASE_DIR, "log/info.log")
PATH_ERROR_LOG = os.path.join(BASE_DIR, "log/error.log")
PATH_PCRF_LOG = os.path.join(BASE_DIR, "log/pcrf.log")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)-15s-----%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'pcrf': {
            'format': '%(asctime)s,%(msecs)05.1f %(message)s',
            'datefmt': '%m/%d/%Y %H:%M:%S',
        },
    },
    'handlers': {
        # 'file_info': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': PATH_INFO_LOG,
        #     'maxBytes': 1024 * 1024 * 5,
        #     'formatter': 'verbose',
        # },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PATH_ERROR_LOG,
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'verbose',
        },
        'file_pcrf': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': PATH_PCRF_LOG,
            'maxBytes': 1024 * 1024 * 5,
            'formatter': 'pcrf',
        },
    },
    'loggers': {
        'error': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        # 'info': {
        #     'handlers': ['file_info'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
        'pcrf': {
            'handlers': ['file_pcrf'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

logger = logging.getLogger("pcrf")
logger_error = logging.getLogger("error")