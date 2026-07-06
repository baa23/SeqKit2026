import pytest
from pathlib import Path
from baaSeqKit.main import get_s_from_file, check_DNA

# ------------------------------
# Tests for get_s_from_file()
# ------------------------------

# Test raising error when file does not exist
def test_get_s_from_file_nonexistance():
    # Input false filename to function
    with pytest.raises(SystemExit):
        get_s_from_file("does_not_exist.txt")

# Test exiting when file empty
def test_get_s_from_file_empty():
    # The empty file should cause system exit
    file_path = Path("empty.txt")
    with pytest.raises(SystemExit):
        get_s_from_file(file_path)

# Test return when file exists and has contents
def test_get_s_from_file_acceptable():
    # Function should retrive the string from the file
    file_path = Path("test_string.txt")
    with open(file_path) as file:
        file_string = file.read()
    assert file_string == get_s_from_file(file_path)
    
# ------------------------------
# Tests for check_DNA()
# ------------------------------

# Sequence is/contains lower case
def test_check_DNA_lower():
    # Get input string from file
    with open("non_DNA_string.txt") as file:
        non_DNA = file.read()
    # Pass input to function to test for system exit
    with pytest.raises(SystemExit):
        check_DNA(non_DNA)

# Sequence contains non-DNA alphabet
def test_check_DNA_alphabet():
    # Get input string from file
    with open("non_DNA_string.txt") as file:
        non_DNA = file.read()
    # Pass input to function to test for system exit
    with pytest.raises(SystemExit):
        check_DNA(non_DNA)

# Sequence is valid DNA
def test_check_DNA_acceptable():
    # Get input string from file
    with open("test_string.txt") as file:
        input_DNA = file.read()
    # Check the input string passes check function validation
    assert check_DNA(input_DNA)