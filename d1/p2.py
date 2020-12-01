#!/usr/bin/python3
# Same as p1, but with _3_ elements totalling 2020

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
input_list = list(map(int, input_file.readlines()))
input_length = len(input_list)
print("Read " + str(input_length) + " lines from file.")

# Iterate over list until two elements summing to 2020 are found
for i in range(0, (input_length - 2)):
    for j in range(i + 1, (input_length - 1)):
        for k in range(i + 2, (input_length)):
            sum = input_list[i] + input_list[j] + input_list[k]
            if sum == 2020:
                # Get product of those elements
                product = input_list[i] * input_list[j] * input_list[k]
                # Output
                print("Found " + str(input_list[i]) + " * " + str(input_list[j]) + " * " + str(input_list[k]) + " = " + str(product))
                exit()

print("Something went wrong; no matching sets found.")