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

field_set = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
optional_set = {"cid"}

record_list = [{}]
valid_count = 0
index = 0
#First, make records of adjacent non-blank inputs
for line in input_list:
    if line.strip() == "":
        record_list.append({})
        index += 1
        next
    elements = line.strip().split()
    for element in elements:
        key_val = element.split(':')
        record_list[index].update({key_val[0]:key_val[1]})

print("Created {} records".format(len(record_list)))

# Check records for required and optional fields
for record in record_list:
    record_set = set(record.keys())
    diff = field_set.difference(record_set)
    if diff == set() or diff == optional_set:
        valid_count += 1

print("Valid record: ", valid_count)
