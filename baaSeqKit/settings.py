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
            "level": "INFO",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": LOG_FILE,
        },
    },

    # --------------------------------------------------
    # OPTIONAL: NAMED LOGGER (TEACHING EXAMPLE)
    # --------------------------------------------------
    # Why define a named logger?
    # - Gives fine-grained control over specific parts of your app
    # - Lets you tune verbosity per module/package
    #
    # BEST PRACTICE:
    # - Name your logger after your *top-level package*
    #   e.g. package: seqkitstp → logger: "seqkitstp"
    #
    # WHY?
    # - Keeps logs consistent and predictable
    # - Makes filtering/searching easier
    # - Matches how logging.getLogger(__name__) resolves names
    #
    # HOWEVER:
    # You can deliberately override naming if it improves clarity.
    #
    # Example:
    # - Your package is "seqkitstp"
    # - But you want cleaner logs → use "SeqKit"
    #
    # Trade-off:
    # ✔ Cleaner log labels
    # ✖ Slightly less direct mapping to Python module paths


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