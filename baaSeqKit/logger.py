"""
This file creates (or retrives) the logger.

It then checks no handlers already exist (i.e. first import/run).
If not then it will configure handlers and add to the logger

The logger can then be used in another file/script
"""

import logging
import os

# Create (or retrieve) the logger
logger = logging.getLogger("baaSeqKit")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers if imported multiple times
# Will only run if handlers don't exist i.e. first import
if not logger.handlers:

    # Find project root (1 level up from this file)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, ".."))

    # Create logs directory
    logs_dir = os.path.join(project_root, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Log file path
    log_file = os.path.join(logs_dir, "baaseqkit.log")

    # Log message format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"
    )

    # Console handler (prints to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # File handler (writes to file)
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    # Attach handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)