import logging

logger = logging.getLogger(__name__)

def string_to_blocks(settings):
    """
    Return string from file with delimiter inserted after every nth character
    """
    logger.debug("string_to_blocks function called")

    # List to add string slices to
    block_slices = []

    # Add each slice of string to list
    for i in range(0, len(settings["s"]), int(settings["n"])):
        block_slices.append(settings["s"][i:i+int(settings["n"])])
    
    # Join string slices seperated by delimiter
    new_string = settings["d"].join(block_slices)
    
    return new_string