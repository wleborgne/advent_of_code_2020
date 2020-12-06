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

record_list = [set()]
index = 0
#First, make records of adjacent non-blank inputs
for line in input_list:
    answers = line.strip()
    if answers == "":
        # Add an empty set for next groups answers and advance index
        record_list.append(set())
        index += 1
        next
    # transform line into a list of chars, make a set, union with 
    # what's already there to dedup
    record_list[index] = record_list[index].union(set(list(answers)))

print("Created {} records".format(len(record_list)))

# Total up sizes of answer sets
answer_sum = 0
for a in record_list:
    answer_sum += len(a)
print("Answer sum: ", answer_sum)
