
import logging
import sys
from pathlib import Path
from baaSeqKit.logger import setup_logging
from baaSeqKit.modules import block_string, format_string

# Get a logger for this module
logger = logging.getLogger(__name__)

def main():
    """
    Main application entry point.
    """

    # Initialise logging
    setup_logging()
    logger.info("Program started")

    # Dictionary for storing parameters
    parameters = {}

    # Ask user how string will be given (convert input to lowercase)
    source_type = input(
        "Do you wish to submit your string via file or input "
        "(type f for file or i for input): "
    ).lower()

    # Only allow input of f/F or i/I
    while source_type != "f" and source_type != "i":
        print("invalid input")
        source_type = input(
            "type f for file or i for input: "
        ).lower()

    # Get string from file or input as determined by user
    if source_type == "f":
        # run function to extract string from file
        parameters["s"] = get_s_from_file(input("Enter filename: "))
        logger.debug("string length is %d", len(parameters["s"]))

    # Else get string as input from user
    elif source_type == "i":
        parameters["s"] = input("Submit string: ")

    # Determine how user wants string formatted
    method = input(
        "How would you like your string formatted?\n"
        "1. Split into a given block size\n"
        "2. Into columns of blocks of a given size\n"
        "Enter number: "
        )
    
    # Ensure user given 1 or 2 only
    while method != "1" and method != "2":
        method = input(
        "Enter 1 or 2: "
        )
    
    # Execute function to convert string into blocks
    if method == "1":
        # Determine block size needed
        while True:
            n = input("Give size of blocks required: ")

            # Ensure number is given
            if not n.isdigit():
                print("Invalid input")
                continue
            
            # Ensure number is not longer than the string
            if int(n) >= len(parameters["s"]):
                print("block size must be smaller than total string length")
                continue

            # Both conditions satisfied
            parameters["n"] = n
            break

        # Get delimiter to include from user
        parameters["d"] = input("Enter required delimiter: ")

        # Call function, passing in parameters dictionary
        modified_string = block_string.string_to_blocks(parameters)
        logger.debug("return from string_to_blocks function complete")

        # Add outout to file
        with open("new_string.txt", "w") as f:
            f.write(modified_string)
            logger.info("string output updated to file new_string.txt")

        # Print output to console
        print(f"new string:\n{modified_string}")

    # Execute function to format as blocks in columns
    if method == "2":
        # Determine block size needed
        while True:
            n = input("Give size of blocks required: ")

            # Ensure number is given
            if not n.isdigit():
                print("Invalid input")
                continue
            
            # Ensure number is not longer than the string
            if int(n) >= len(parameters["s"]):
                print("block size must be smaller than total string length")
                continue

            # Both conditions satisfied
            parameters["n"] = n
            break

        # Determine number of columns per row
        parameters["c"] = input("how many blocks per row: ")

        # Get delimiter to include from user
        parameters["d"] = input("Enter required delimiter: ")

        # Determine case for output string
        string_case = input(
            "Which case would you like the string output in, "
            "(type 1 for lowercase or 2 for UPPERCASE): "
            )
        
        # Ensure only 1 or 2 option selected
        while string_case != "1" and string_case != "2":
            print("Invalid input")
            string_case = input(
                "type 1 for lowercase or 2 for UPPERCASE: "
                )

        # Updates parameter dictionary with relevant case
        match string_case:
            case "1":
                parameters["case"] = "lower"
            case "2":
                parameters["case"] = "upper"

        # Use string_to_block to make chunks
        parameters["s"] = block_string.string_to_blocks(parameters)

        # Convert new_string to GenBank format
        genbank_string = format_string.convert_to_GenBank(parameters)
        logger.debug("return from convert_to_GenBank function complete")

        # Dynamically determine formatting for starting numbers
        sig_fig = len(str(max(genbank_string)))
       
        with open("genbank_string.txt", "w") as f:
            for key, value in genbank_string.items():
                line = (f"{key:{sig_fig}} {value}")
                f.write(line + "\n")
                print(line)

        logger.info("string output updated to file genbank_string.txt")
    
    logger.info("Program completed")


def get_s_from_file(f):
    """
    Get string from given file name
    """

    # Get string from file
    try:
        s = Path(f).read_text().strip() # find file and assign to s
        logger.info("file contents parsed")
    except FileNotFoundError:
        logger.error("file not found")
        logger.critical("program aborted")
        sys.exit(1)
    
    if s == "": # raise error if file is empty
        logger.error("file contents not valid")
        logger.critical("program aborted")
        sys.exit(1)
    
    return s

if __name__ == "__main__":
    main()