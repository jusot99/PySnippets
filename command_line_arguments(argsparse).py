# Command Line Arguments (argparse) Guide

import argparse

# 1. Creating a parser
parser = argparse.ArgumentParser(description="A program with command line arguments.")

# 2. Adding positional arguments
parser.add_argument("input_file", help="Path to the input file")

# 3. Adding optional arguments
parser.add_argument("-o", "--output", help="Path to the output file")

# 4. Adding arguments with choices
parser.add_argument("--mode", choices=["read", "write"], help="Operation mode")

# 5. Adding arguments with default values
parser.add_argument("--threshold", type=float, default=0.5, help="Threshold value")

# 6. Adding boolean flags
parser.add_argument("--verbose", action="store_true", help="Enable verbose mode")

# 7. Parsing the command line arguments
args = parser.parse_args()

# 8. Accessing the values of arguments
input_file = args.input_file
output_file = args.output
mode = args.mode
threshold = args.threshold
verbose = args.verbose

# 9. Using the parsed arguments
print("Input File:", input_file)
print("Output File:", output_file)
print("Mode:", mode)
print("Threshold:", threshold)
print("Verbose Mode:", verbose)

# Note: Run the program with different command line arguments to see how argparse works.

# This program showcases various features of the argparse module, 
# including positional arguments, optional arguments, arguments with choices, 
# arguments with default values, and boolean flags. The comments provide explanations for each section. 
# To run this program with command line arguments, use a terminal or 
# command prompt and execute the script, providing the desired arguments. 
# For example: python script.py input.txt -o output.txt --mode write --threshold 0.8 --verbose
