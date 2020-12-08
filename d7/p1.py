#!/usr/bin/python3
import sys
import os.path

# def find_containers(rule_list, current_adj, current_color):
#     print("current target: ", current_adj, current_color)
#     temp_list = []
#     for container in rule_list.keys():
#         contents = rule_list[container]
#         if current_adj in contents.keys() and contents[current_adj] == current_color:
#             temp_list.append(container)
#             print("current temp list: ", temp_list)

#     if len(temp_list) == 0:
#         return []

#     for outer in temp_list:
#         print("current outer bag: ", outer)
#         next_target = outer.split()
#         result = find_containers(rule_list, next_target[0], next_target[1])
#         print("current result: ", result)
#         if len(result) > 0:
#             temp_list = temp_list + result
#         print("recursive temp list: ", temp_list)
#     return temp_list

def find_containers(rule_list, current_adj, current_color):
    print("current target: ", current_adj, current_color)
    temp_list = []

    for container in rule_list.keys():
        contents = rule_list[container_list]
        if current_adj in contents.keys() and contents[current_adj] == current_color:
            temp_list.append(container)

    for container in temp_list:
        target = container.split()
        result = find_containers(rule_list, target[0], target[1])

        
    return temp_list



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

# parse each line
# (adj) (color) bags contain [(quantity) (adj) (color) bags(,|.)]
target_adj = "shiny" # we're looking for shiny gold bags
target_color = "gold"
empty_sentinel = "no other bags" #

rule_dict = {}
# parse lines into {outer container : contents} dict
for rule in input_list:
    parsed = rule.strip(".\n").split(" bags contain ")
    # insert [container, contents] into dict
    rule_dict.update({parsed[0] : parsed[1]})

# parse contents values into { adjective : color} dicts, or {}
for key in rule_dict.keys():
    contents = rule_dict[key]
    if contents == empty_sentinel:
        rule_dict.update({key : {}})
    else:
        # get list of contained bags
        content_list = contents.split(", ")
        content_dict = {}
        for item in content_list:
            # split into [(quantity) (adj) (color) bag(s)]
            i = item.split()
            content_dict.update({i[1] : i[2]})
        rule_dict.update({key : content_dict})

# first pass: find keys in main dict that have target directly in value dict
container_list = find_containers(rule_dict, target_adj, target_color)
container_set = set(container_list)
#print(rule_dict)
print("Total: ", len(container_set))