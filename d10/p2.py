#!/usr/bin/python3
import sys
import os.path
import itertools

def valid(plug_list):
    v = True
    # add first, last elements
    plug_list.insert(0, 0)
    plug_list.append(perm[-1] + 3)

    for i in range(len(plug_list) - 1):
        if 1 <= (plug_list[i + 1] - plug_list[i]) <= 3:
            next
        else:
            valid = False
            break
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
valid_set = set()
invalid_set = set()
# Calculate smallest set of input that could possibly
# be valid; i.e., all diffs = 3
min_valid_length = (input_list[-1] // 3) + 1

# for length in range(min_valid_length, input_length):
#     # for each permutation of length in input
#     for perm in itertools.permutations(input_list, length):
#         perm_list = list(perm)
#         perm_list.sort()
#         perm_list_tuple = tuple(perm_list)
#         # we may have already seen this one
#         if perm_list_tuple in valid_set or perm_list_tuple in invalid_set:
#             next
#         if valid(perm_list):
#             valid_set.add(perm)
#         else:
#             invalid_set.add(perm)
#         print("valid: ", len(valid_set))
#         print("invalid: ", len(invalid_set))

# print("Valid combinations: ", len(valid_set))

# DOESN'T WORK, TOO LONG
# insert into a set to dedup
# for each member in set:
# add 0 and max_val + 3
# validate 1 <= diff adjacent elements <= 3

# sort list
# add 0, max
# get set of possible second elements (1, 2, 3)
# for each possible n element,
# get set of possible n + 1 elements (n+1, n+2, n+3)
# etc
# possible first: 1, 2, 3
# if no 2 or 3, 




input_list.insert(0, 0)
input_list.append(input_list[-1] + 3)





