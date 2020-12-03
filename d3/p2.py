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
repeat = len(input_list[0]) - 1
path_list = [[1, 1],[3, 1],[5, 1],[7, 1],[1, 2]]
tree_product = 1

# for each path element in path_list
for path in path_list:
    x_inc = path[0]
    y_inc = path[1]
    # starting at x = 0,y = 0
    x = 0
    y = 0
    tree_sum = 0
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
            tree_sum += 1

    # report tree total for this path
    print('Path {},{} encountered {} trees'.format(x_inc, y_inc, tree_sum))
    # calculate latest product
    tree_product *= tree_sum

# Report result
print("Tree product: ", tree_product)
