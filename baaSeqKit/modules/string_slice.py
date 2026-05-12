""" 
This file contains functions to slice a string into specified blocks
"""
import logging

# Step 2: Get the logger (this is the key idea)
logger = logging.getLogger(__name__)

def slice_string(s, d, n):
    """
    Return the string s with the delimitor d inserted after every nth character
    """
    logger.info("slice_string function called")
    logger.debug("slice_string() called with s, d=%s, n=%d", d, n)

    blocks = []

    for i in range(0, len(s), n):
        blocks.append(s[i:i+n])
  
    modified_string = d.join(blocks)
    
    return modified_string

if __name__ == "__main__":
    slice_string()