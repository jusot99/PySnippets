# Logging Guide

import logging

# 1. Configuring the logging system
# BasicConfig sets up a simple configuration that outputs log messages to the console.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 2. Logging messages at different levels
logging.debug("This is a debug message")      # Only shown if logging level is DEBUG or lower
logging.info("This is an info message")        # Shown if logging level is INFO or lower
logging.warning("This is a warning message")   # Shown if logging level is WARNING or lower
logging.error("This is an error message")       # Shown if logging level is ERROR or lower
logging.critical("This is a critical message") # Shown if logging level is CRITICAL

# 3. Logging variables and formatting
name = "Alice"
age = 30
logging.info("User: %s, Age: %d", name, age)

# 4. Logging exceptions
try:
    result = 10 / 0
except ZeroDivisionError as e:
    logging.error("Exception occurred: %s", e, exc_info=True)

# 5. Logging to a file
file_handler = logging.FileHandler("example.log")
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

logging.getLogger('').addHandler(file_handler)
logging.warning("This message will be logged to both the console and the file")

# 6. Logging to different files for different log levels
error_file_handler = logging.FileHandler("error.log")
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(file_format)

logging.getLogger('').addHandler(error_file_handler)
logging.error("This message will be logged to the error.log file")

# Note: Adjust the logging levels and messages to suit your application's needs.
# The logging module provides a powerful and flexible way to handle application logging.
