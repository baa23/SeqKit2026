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
from baaSeqKit.modules import string_GenBank

# --------------------------------------------------
# STEP 3: Main execution function
# --------------------------------------------------
def main():
    """
    Main application entry point.

    """

    # Initialise logging (CRITICAL STEP)
    setup_logging()

    string_GenBank.main()

# --------------------------------------------------
# ENTRY POINT GUARD
# --------------------------------------------------
# Ensures this script only runs when executed directly

if __name__ == "__main__":
    main()