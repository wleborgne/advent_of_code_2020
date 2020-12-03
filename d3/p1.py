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

clear = "."
tree = "#"
x = 0
x_inc = 3
y = 0
y_inc = 1
tree_total = 0
repeat = len(input_list[0]) - 1

# starting at x = 0,y = 0
while True:
    # calculate x = (x + x_inc) mod repeat, y = y + y_inc
    x = (x + x_inc) % repeat
    y += y_inc
    # if y > input_length, done
    if y > input_length - 1:
        break
    char = input_list[y][x]
    # if char == tree, increment tree_total
    if char == tree:
        tree_total += 1

# report tree total
print("Trees encountered: ", tree_total)
