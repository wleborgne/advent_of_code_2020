#!/usr/bin/python3
import sys
import os.path

# GLOBAL VARS!!!!
ACCUMULATOR = 0
INST_POINTER = 0

def nop():
    global INST_POINTER
    INST_POINTER += 1
    # print("after nop: ", ACCUMULATOR, INST_POINTER)
    return

def acc(arg):
    global ACCUMULATOR
    global INST_POINTER
    ACCUMULATOR += arg
    INST_POINTER += 1
    # print("after acc: ", ACCUMULATOR, INST_POINTER)
    return

def jmp(arg):
    global INST_POINTER
    INST_POINTER += arg
    # print("after jmp: ", ACCUMULATOR, INST_POINTER)
    return

def compile(source):
    inst_list = []
    for line in source:
        parsed = line.split()
        inst = {"op": parsed[0], "arg": int(parsed[1])}
        inst_list.append(inst)
    return inst_list

def debug(prog):
    global INST_POINTER
    global ACCUMULATOR
    executed = {}
    while True:
        if INST_POINTER == len(prog):
            print("Reached program end. Accumulator: ", ACCUMULATOR)
            exit()

        if INST_POINTER in executed.keys():
            print("Loop found at location: ", INST_POINTER)
            print("Current accumulator value: ", ACCUMULATOR)
            return
        
        executed.update({INST_POINTER: True})
        execute(prog[INST_POINTER])


def execute(inst):
    # print("Current state: ", ACCUMULATOR, INST_POINTER)
    op = inst["op"]
    arg = inst["arg"]
    if op == "nop":
        nop()
    elif op == "jmp":
        jmp(arg)
    elif op == "acc":
        acc(arg)
    
def find_bad(prog):
    loc_list = []
    for i in range(len(prog)):
        if prog[i]["op"] in ["nop", "jmp"]:
            loc_list.append(i)
    return loc_list

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

program = compile(input_list)
# Find locations of nop/jmp
bug_loc = find_bad(program)
print(bug_loc)

# For each location
for loc in bug_loc:
    # Make a copy of original program
    current_copy = []
    for inst in program:
        current_copy.append(inst.copy())
    # Swap nop <-> jmp
    print("Replacing instruction at ", loc)
    if current_copy[loc]["op"] == "nop":
        current_copy[loc]["op"] = "jmp"
    elif current_copy[loc]["op"] == "jmp":
        current_copy[loc]["op"] = "nop"
    else:
        print("Something went wrong!")
        exit

    # Debug
    ACCUMULATOR = 0
    INST_POINTER = 0
    debug(current_copy)

print("Done.")