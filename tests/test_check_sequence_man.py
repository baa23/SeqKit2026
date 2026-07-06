import pytest
from pathlib import Path
from baaSeqKit.modules.sequence_manipulation import transcribe_DNA, translate_RNA
from baaSeqKit.main import check_DNA

# ------------------------------
# Tests for check_DNA()
# ------------------------------

# Sequence is/contains lower case
def test_check_DNA_lower():
    # Test input string
    non_DNA = "this is not DNA"
    # Pass input to function to test for system exit
    with pytest.raises(SystemExit):
        check_DNA(non_DNA)

# Sequence contains non-DNA alphabet
def test_check_DNA_alphabet():
    # Test input string
    non_DNA = "this is not DNA"
    # Pass input to function to test for system exit
    with pytest.raises(SystemExit):
        check_DNA(non_DNA)

# Sequence is valid DNA
def test_check_DNA_acceptable():
    # Test input sequence
    input_DNA = "AGGTGCATCGTGCAATAAGGA"
    # Check the input string passes check function validation
    assert check_DNA(input_DNA)

# ------------------------------
# Tests for transcribe_DNA()
# ------------------------------

def test_transcribe_DNA():
    # Test input sequence
    sequence = "AGGTGCATCGTGCAATAAGGA"
    # Result from calling function
    result = transcribe_DNA(sequence)

    assert sequence.replace("T", "U").lower() == result

