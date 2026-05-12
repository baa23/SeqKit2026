# logger.py
"""
This file contains the function (and module/data structure) needed to set-up logger

We load configuration from settings.py and apply it
WHEN explicitly requested.

"""

import logging.config

from baaSeqKit.settings import LOGGING_CONFIG

# --------------------------------------------------
# LOGGING ACTIVATION FUNCTION
# --------------------------------------------------
def setup_logging():
    """
    Apply the logging configuration.
    """

    logging.config.dictConfig(LOGGING_CONFIG)