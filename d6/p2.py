#!/usr/bin/python3
import sys
import os.path
import string
import itertools

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

record_list = [[]]
index = 0
#First, make records of adjacent non-blank inputs
for line in input_list:
    answer_set = set(list(line.strip()))
    if answer_set == set():
        # Add an empty list for next groups answers and advance index
        record_list.append([])
        index += 1
        next
    else:
        # add non-empty sets to current group list
        record_list[index].append(answer_set)

print("Created {} records".format(len(record_list)))

answer_sum = 0
# make an empty dictionary to count answers
zero_dict = {}
for char in string.ascii_lowercase:
    zero_dict.setdefault(char, 0)
for record in record_list:
    if len(record) == 1:
        # for single-person groups, add length of set
        answer_sum += len(record[0])
    else:
        # for multi-person groups
        num_sets = len(record)
        temp_dict = zero_dict.copy()
        # for each answer set
        for s in record:
            # increment dictionary entry for each set member
            for i in s:
                temp_dict[i] += 1
        # take dict entries where value equals number of members
        for k in temp_dict.keys():
            if temp_dict[k] == num_sets:
                answer_sum += 1

print("Count: ", answer_sum)
