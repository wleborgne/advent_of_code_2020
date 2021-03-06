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

translation = str.maketrans({'F':'0', 'L':'0', 'B':'1', 'R':'1'})
max_id = 0

for seat in input_list:
    # substitute 0/1 for FL/BR
    seat_trans = seat.translate(translation)
    # split into row, column and convert from binary
    row_val = int(seat_trans[0:7], base = 2)
    col_val = int(seat_trans[7:], base = 2)
    # calculate ID, and compare to current max
    id = (row_val * 8) + col_val
    if id > max_id:
        max_id = id

print("Max seat ID: ", max_id)
