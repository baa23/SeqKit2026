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

# --------------------------------------------------
# STEP 1: Import logging setup function
# --------------------------------------------------
# No side effects — this only imports the function

from baaSeqKit.logger import setup_logging


# --------------------------------------------------
# STEP 2: Import application modules
# --------------------------------------------------
# These modules will create loggers using __name__,
# but they will only behave correctly AFTER setup_logging()

from baaSeqKit.modules import logging_demo


# --------------------------------------------------
# STEP 3: Main execution function
# --------------------------------------------------
def main():
    """
    Main application entry point.

    """

    # Initialise logging (CRITICAL STEP)
    setup_logging()

    # Run demo module
    logging_demo.logging_demo()


# --------------------------------------------------
# ENTRY POINT GUARD
# --------------------------------------------------
# Ensures this script only runs when executed directly

if __name__ == "__main__":
    main()