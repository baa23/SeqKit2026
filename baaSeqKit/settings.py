# settings.py
"""
More optimised way for performing logging
"""

import os

# --------------------------------------------------
# STEP 1: Define default log file (hidden, home directory)
# --------------------------------------------------
home_dir = os.path.expanduser("~")
DEFAULT_LOG = os.path.join(home_dir, ".baaseqkit.log")

LOG_FILE = DEFAULT_LOG


# --------------------------------------------------
# STEP 2: NORMALISE the path (defensive step)
# --------------------------------------------------
LOG_FILE = os.path.abspath(os.path.expanduser(LOG_FILE))


# --------------------------------------------------
# STEP 3: Ensure directory exists
# --------------------------------------------------
log_dir = os.path.dirname(LOG_FILE)
if log_dir:
    os.makedirs(log_dir, exist_ok=True)


# --------------------------------------------------
# STEP 4: Logging configuration
# --------------------------------------------------
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    # --------------------------------------------------
    # FORMATTERS
    # --------------------------------------------------
    "formatters": {
        "standard": {
            "format": (
                "%(asctime)s | %(levelname)s | %(name)s | "
                "%(filename)s:%(lineno)d | %(message)s"
            )
        }
    },

    # --------------------------------------------------
    # HANDLERS
    # --------------------------------------------------
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "standard",
        },

        # --------------------------------------------------
        # ROTATING FILE HANDLER (UPDATED)
        # --------------------------------------------------
        #
        # This replaces the basic FileHandler with a
        # RotatingFileHandler to prevent unlimited growth.
        #

        "file": {
            "class": "logging.handlers.RotatingFileHandler",

            # Only store ERROR and CRITICAL messages in file
            # (keeps disk usage focused on important events)
            "level": "DEBUG",

            "formatter": "standard",
            "filename": LOG_FILE,
            # --------------------------------------------------
            # ROTATION SETTINGS (IMPORTANT TEACHING POINT)
            # --------------------------------------------------
            #
            # maxBytes:
            # Maximum size of the log file BEFORE rotation happens.
            #
            # Example:
            # 1_048_576 bytes = 1 MB
            #
            # Here we set a small size for demonstration.
            #
            "maxBytes": 1024 * 5,  # 50 KB
            "backupCount": 3,

            # Optional: ensures file opens safely even if reused
            "encoding": "utf-8",
        },
    },
        

    # --------------------------------------------------
    # OPTIONAL: NAMED LOGGER (TEACHING EXAMPLE)
    # --------------------------------------------------

    "loggers": {
        "baaSeqKit": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": False
        },
    },

    # --------------------------------------------------
    # ROOT LOGGER
    # --------------------------------------------------
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    }
}