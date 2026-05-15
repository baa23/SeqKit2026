""" 
This file contains functions to slice a string into specified blocks and GenBank format
"""
import logging
import sys
from pathlib import Path
from baaSeqKit.logger import setup_logging

# Get a logger for this module
logger = logging.getLogger(__name__)

# Parameters for modifying the string
BLOCK_SIZE = 10
DELIMITER = " "

def main():

    # Initialise logging
    setup_logging()

    logger.info("Program started")

    # Get string and return string in blocks
    modified_string = string_to_blocks("string.txt", DELIMITER, BLOCK_SIZE)
    logger.debug("return from string_to_blocks function complete")

    # Convert modified_string to GenBank format
    genbank_string = convert_to_GenBank(modified_string)
    logger.debug("return from convert_to_GenBank function complete")

    for row in genbank_string:
        print(row)

    logger.debug("output printed to console")


def string_to_blocks(f, d, n):
    """
    Return string from file with delimiter inserted after every nth character
    """
    logger.debug("string_to_blocks function called")

    # Get string from file
    try:
        s = Path(f).read_text().strip()
        logger.info("file contents parsed")
    except FileNotFoundError:
        logger.error("file not found")
        logger.critical("program aborted")
        sys.exit(1)
    
    if s == "":
        logger.error("file contents not valid")
        logger.critical("program aborted")
        sys.exit(1)

    block_slices = []

    for i in range(0, len(s), n):
        block_slices.append(s[i:i+n])
  
    new_string = d.join(block_slices)
    
    return new_string

def convert_to_GenBank(s):
    """
    Return string in GenBank format
    """
    logger.debug("convert_to_GenBank function called")

    # Seperate string into it's base blocks for columns
    blocks = s.lower().split()

    # Build each row by arranging list of blocks into 6 columns
    genbank_rows = []

    index = 0
    row = 0

    number_of_blocks = len(blocks)

    while index < number_of_blocks:
        blocks_added = False
        growing_string = []

        for _ in range(6):
            if index >= number_of_blocks:
                break

            if not blocks_added:
                growing_string.append(str(1 + (row * 60)).rjust(4))
                logger.debug("string starts with %s", growing_string[0])
    
            growing_string.append(blocks[index])
            blocks_added = True

            index += 1
        
        genbank_rows.append(" ".join(growing_string))
        row += 1

    logger.debug("while loop completed")

    return genbank_rows

if __name__ == "__main__":
    main()