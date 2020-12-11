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
input_list = list(map(int, input_file.readlines()))
input_length = len(input_list)
print("Read " + str(input_length) + " lines from file.")

input_list.sort()
input_list.insert(0, 0)
input_list.append(input_list[-1] + 3)
one_count = 0
three_count = 0

# this is the *original* input length
for i in range(input_length + 1):
    diff = input_list[i + 1] - input_list[i]
    if diff == 1:
        one_count += 1
    elif diff == 3:
        three_count += 1

print("one_count: ", one_count)
print("three_count: ", three_count)
print("product: ", one_count * three_count)
