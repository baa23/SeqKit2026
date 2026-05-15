# main.py
"""
MAIN ENTRY POINT FOR SeqKitSTP

----------------------------------------
TEACHING TAKEAWAY
----------------------------------------

✔ Configure once → at application start
✔ Never reconfigure → prevents overwriting
✔ Use __name__ everywhere → automatic hierarchy

→ Simple, safe, and scalable logging
"""
import logging
from baaSeqKit.logger import setup_logging
from baaSeqKit.modules import string_GenBank

# Get a logger for this module
logger = logging.getLogger(__name__)

def main():
    """
    Main application entry point.
    """

    # Initialise logging (CRITICAL STEP)
    setup_logging()

    string_GenBank.main()
    logger.info("Program completed")

if __name__ == "__main__":
    main()