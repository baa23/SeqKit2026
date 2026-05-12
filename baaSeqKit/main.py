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
from pathlib import Path

from baaSeqKit.logger import setup_logging

from baaSeqKit.modules.string_slice import slice_string

BLOCK_SIZE = 10

# --------------------------------------------------
# STEP 3: Main execution function
# --------------------------------------------------
def main():
    """
    Main application entry point.

    """

    # Initialise logging (CRITICAL STEP)
    setup_logging()

    # parse string from file and call slice function
    data = Path("string.txt").read_text().strip()
    print(slice_string(data, " ", BLOCK_SIZE))


# --------------------------------------------------
# ENTRY POINT GUARD
# --------------------------------------------------
# Ensures this script only runs when executed directly

if __name__ == "__main__":
    main()