
import logging
import sys
from pathlib import Path
from baaSeqKit.logger import setup_logging
from baaSeqKit.modules import block_string, format_string

# Get a logger for this module
logger = logging.getLogger(__name__)

def main():
    """
    Main application entry point.
    """

    # Initialise logging
    setup_logging()
    logger.info("Program started")

    # TODO develop transcribe function and include tests


def get_s_from_file(f):
    """
    Get string from given file name
    """

    # Get string from file
    try:
        s = Path(f).read_text().strip() # find file and assign to s
        logger.info("file contents parsed")
    except FileNotFoundError:
        logger.error("file not found")
        logger.critical("program aborted")
        sys.exit(1)
    
    if s == "": # raise error if file is empty
        logger.error("file contents not valid")
        logger.critical("program aborted")
        sys.exit(1)
    
    return s

if __name__ == "__main__":
    main()