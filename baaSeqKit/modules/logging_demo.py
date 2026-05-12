# modules/logging_demo.py
"""
LOGGING DEMONSTRATION SCRIPT

----------------------------------------
WHAT THIS SCRIPT DOES
----------------------------------------
This script demonstrates how to use logging properly
by retrieving a logger and using different log levels.

----------------------------------------
FRAMEWORK / WEB APP NOTE
----------------------------------------

✔ In larger applications (e.g. web apps):
  - The parent application may override logging
  - Your module-level loggers will integrate naturally

✔ This works because:
  - logger names follow the package hierarchy
  - configuration is centralised and inheritable
"""

# Step 2: Get the logger (this is the key idea)
import logging
logger = logging.getLogger(__name__)


def logging_demo():
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

    return None

if __name__ == '__main__':
    logging_demo()