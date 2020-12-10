#!/usr/bin/python3
import sys
import os.path
import networkx as nx

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

target_node = "shiny gold" # we're looking for shiny gold bags

bag_graph = nx.DiGraph()
node_list = []

# parse lines and build node list
for rule in input_list:
    parsed = rule.strip(".\n").split(" bags contain ")
    parent = parsed[0]
    children = parsed[1].split(", ")
    for child in children:
        ch_parts = child.split()
        if ch_parts[0] == "no":
            break
        weight = int(ch_parts[0])
        node_name = ch_parts[1] + " " + ch_parts[2]
        node_list.append((parent, node_name, weight))

bag_graph.add_weighted_edges_from(node_list)
ancestor_set = nx.algorithms.dag.ancestors(bag_graph, target_node)
print("Got containing bag count: ", len(ancestor_set))