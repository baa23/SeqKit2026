import logging

# Get a logger for this module
logger = logging.getLogger(__name__)

def transcribe_DNA(sequence):
    """
    Convert a DNA sequence into it's corresponding RNA

    Parameters
        sequence : str
            valid DNA sequence
    Returns
        string
            converted RNA
    """
    logger.info("transcribe_DNA function called")
    
    sequence = sequence.replace("T", "U").lower()

    return sequence

def translate_RNA(sequence):
    # TODO take RNA and convert to protein
    logger.info("Translate_RNA function called")
    return True