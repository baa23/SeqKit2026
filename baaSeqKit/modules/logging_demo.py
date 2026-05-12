# logging_demo.py
"""
This file runs a demo of how a logger will pass log records
The handlers control how the messages appear on the terminal (streamHandler) and file (fileHandler)

The file retrives the logger created when doing import logger

Run the file as module to see demo
Adjusting logger and handler levels in logger.py will influence messages logged on these streams
"""

# Step 1: Import the logging setup (this runs configuration once)
from baaSeqKit import logger  # ensures logging is configured

# Step 2: Get the logger (this is the key idea)
import logging
logger = logging.getLogger("baaSeqKit")


# --------------------------------------------------
# DEMO: Different logging levels
# --------------------------------------------------

logger.debug("DEBUG: Detailed info for debugging problems.")

logger.info("INFO: The program has started successfully.")

logger.warning("WARNING: Something unexpected happened, but continuing.")

logger.error("ERROR: Something failed during execution.")

logger.critical("CRITICAL: Serious failure - program may stop.")


# --------------------------------------------------
# FINAL MESSAGE
# --------------------------------------------------

logger.info("Demo complete. Check the console and log file.")