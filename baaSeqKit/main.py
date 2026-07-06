
import logging
import sys
from pathlib import Path
from baaSeqKit.logger import setup_logging
from baaSeqKit.modules import sequence_manipulation

# Get a logger for this module
logger = logging.getLogger(__name__)

class NonDNAError(Exception):
    pass


def main():
    """
    Main application entry point.
    """

    # Initialise logging
    setup_logging()
    logger.info("Program started")

    # Ask user how string will be given (convert input to lowercase)
    source_type = input(
        "Do you wish to submit your DNA string via file or input "
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
        input_string = get_s_from_file(input("Enter filename: ")).strip()
        logger.debug("String length is %d", len(input_string))

    # Else get string as input from user
    elif source_type == "i":
        input_string = input("Submit string: ").strip()
        logger.debug("String length is %d", len(input_string))

    # Check user has submitted a DNA sequence
    check_DNA(input_string)
    logger.info("Input sequence passed check for valid DNA")

    converted_RNA = sequence_manipulation.transcribe_DNA(input_string)
    print(f"RNA: {converted_RNA}")


def check_DNA(sequence):
    """
    Ensure user has input a DNA sequence
    
    Parameters 
        sequence : str
            DNA sequence to validate
    Returns
        bool
            True if sequence is valid DNA
    Raises
        NonDNAError
            If sequence contains invalid characters or is not uppercase
    """
    logger.info("Check_DNA function called")

    # Check if all characters are uppercase
    try:
        if not sequence.isupper():
            raise NonDNAError("Input not a valid DNA sequence")
    # If sequence not all uppercase create error log
    except NonDNAError:
        logger.error("input is not a valid DNA sequence")
        logger.critical("program aborted")
        sys.exit(1)

    # Check if sequence contains only DNA bases
    try:
        # Iterate over string and check every character is valid
        for base in sequence:
            if base not in ["A", "T", "G", "C"]:
                raise NonDNAError("Input not a valid DNA sequence")
    except NonDNAError:
        logger.error("input is not a valid DNA sequence")
        logger.critical("program aborted")
        sys.exit(1)

    return True

def get_s_from_file(f):
    """
    Get string from given file name
    """

    # Get string from file
    try:
        s = Path(f).read_text().strip() # find file and assign to s
        logger.info("File contents parsed")
    except FileNotFoundError:
        logger.error("File not found")
        logger.critical("Program aborted")
        sys.exit(1)
    
    if s == "": # raise error if file is empty
        logger.error("File contents not valid")
        logger.critical("Program aborted")
        sys.exit(1)
    
    return s

if __name__ == "__main__":
    main()