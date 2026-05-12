""" 
This file contains functions to slice a string into specified blocks
"""
import logging

# Step 2: Get the logger (this is the key idea)
import logging
logger = logging.getLogger(__name__)

def slice_string(s, d, n):
    """
    Return the string s with the delimitor d inserted after every nth character
    """
    logging.info("slice_string function called")
    logging.debug("slice_string() called with s=%r, d=%s, n=%d", s, d, n)

    blocks = []

    for i in range(0, len(s), n):
        blocks.append(s[i:i+n])
        logging.debug("slice starting index (i) is %d, end index is %d", i, i+n)
  
    modified_string = d.join(blocks)
    
    return modified_string

if __name__ == "__main__":
    slice_string()