import logging

logger = logging.getLogger(__name__)

def convert_to_GenBank(settings):
    """
    Return string in GenBank format
    """
    logger.debug("convert_to_GenBank function called")

    # Seperate string into it's base blocks for columns
    if settings["case"] == "lower":
        blocks = settings["s"].lower().split(settings["d"])
    else:
        blocks = settings["s"].upper().split(settings["d"])

    # Dictionary to store starting number with row
    genbank_rows = {}

    # Counters for loops
    index = 0
    row = 0

    # Max index allowed
    number_of_blocks = len(blocks)

    # Number of characters per row to update starting number
    count_per_row = int(settings["n"]) * int(settings["c"])

    # Loop through blocks and build into columns x row format
    while index < number_of_blocks:
        # List to append row blocks onto
        growing_string = []

        # Index blocks for required columns for row
        for _ in range(int(settings["c"])):
            if index >= number_of_blocks:
                break
    
            growing_string.append(blocks[index])

            index += 1
        
        # Update dict with starting number (key) and built row (value)
        genbank_rows[
            (1 + (row * count_per_row))
        ] = (settings["d"].join(growing_string))
        row += 1

    logger.debug("while loop completed")

    return genbank_rows