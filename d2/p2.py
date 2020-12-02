#!/usr/bin/python3
import sys
import os.path

# Get input file from cmd line args
print("Starting....")
print("arg length: ", str(len(sys.argv)))

if len(sys.argv) == 1:
    print("Input filename required")
    exit()

input_filename = sys.argv[1]
print("Using input file: ", input_filename)

# Check if file exists
if not os.path.isfile(input_filename):
    print("Not a valid input file: ", input_filename)
    exit()

# Read input file into a list, casting to int
input_file = open(input_filename, 'r')
input_list = input_file.readlines()
input_length = len(input_list)
print("Read " + str(input_length) + " lines from file.")

valid_count = 0
# For each line,
for line in input_list:
    # split on ': ' to get policy, password
    temp = line.split(": ")
    policy = temp[0]
    password = temp[1]
    # split policy on space to get positions, symbol
    temp = policy.split()
    symbol = temp[1]
    temp = temp[0].split("-")
    # split positions on '-' to get first, second
    first = int(temp[0]) - 1
    second = int(temp[1]) - 1
    # check if symbol is in first XOR second position
    in_first = (password[first] == symbol)
    in_second = (password[second] == symbol)
    if (in_first or in_second) and (in_first != in_second):
        valid_count += 1

print("Valid password count: ", valid_count)