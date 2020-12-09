#!/usr/bin/python3
import sys
import os.path
import itertools

# Get input file from cmd line args
print("Starting....")
print("arg length: ", str(len(sys.argv)))

if len(sys.argv) < 3:
    print("Missing preamble and/or filename")
    exit()

preamble_size = int(sys.argv[1])
input_filename = sys.argv[2]
print("Using input file: ", input_filename)
print("with preamble value ", preamble_size)

# Check if file exists
if not os.path.isfile(input_filename):
    print("Not a valid input file: ", input_filename)
    exit()

# Read input file into a list, casting to int
input_file = open(input_filename, 'r')
input_list = list(map(int, input_file.readlines()))
input_length = len(input_list)
print("Read " + str(input_length) + " lines from file.")

for i in range(len(input_list)):
    current_chunk = input_list[i:i + preamble_size]
    current_element = input_list[i + preamble_size]
    # get all permutations of 2 elements for current chunk
    perms = list(itertools.permutations(current_chunk, 2))
    sums = []

    # sum the tuples
    for perm in perms:
        sums.append(perm[0] + perm[1])

    # check if current element is in the set of sums
    if current_element in sums:
        # if so, continue
        next
    else:
        # if not, output the current element and end
        print("No sum found for: ", current_element)
        break

print("Done.")

