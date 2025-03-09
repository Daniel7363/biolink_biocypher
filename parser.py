import json

# Load the JSON content from the files
file_path_nodes_edges = 'example2.txt'
file_path_example = 'example.txt'

with open(file_path_nodes_edges, 'r') as file:
    data_nodes_edges = json.load(file)

with open(file_path_example, 'r') as file:
    data_example = json.load(file)

# Initialize storage for node and edge names
nodes = []
edges = []

# Function to recursively find nodes and edges
def find_nodes_and_edges(obj, name=""):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "represented_as":
                if value == "node":
                    nodes.append(name)
                elif value == "edge":
                    edges.append(name)
            else:
                find_nodes_and_edges(value, name if name else key)
    elif isinstance(obj, list):
        for item in obj:
            find_nodes_and_edges(item, name)

# Start finding nodes and edges
find_nodes_and_edges(data_nodes_edges)

# Function to search for objects with names of nodes and edges in the example file
def search_keys(data, keys):
    found_keys = []
    not_found_keys = keys[:]
    if isinstance(data, dict):
        for key, value in data.items():
            if key in keys:
                found_keys.append(key)
                not_found_keys.remove(key)
            if isinstance(value, (dict, list)):
                f_keys, nf_keys = search_keys(value, not_found_keys)
                found_keys.extend(f_keys)
                not_found_keys = nf_keys
    elif isinstance(data, list):
        for item in data:
            f_keys, nf_keys = search_keys(item, not_found_keys)
            found_keys.extend(f_keys)
            not_found_keys = nf_keys
    return found_keys, not_found_keys

# Search for nodes and edges in the example file
found_nodes, not_found_nodes = search_keys(data_example, nodes)
found_edges, not_found_edges = search_keys(data_example, edges)

# Print results
print(f"Found node keys ({len(found_nodes)}):")
for key in found_nodes:
    print(key)

print(f"\nNot found node keys ({len(not_found_nodes)}):")
for key in not_found_nodes:
    print(key)

print(f"\nFound edge keys ({len(found_edges)}):")
for key in found_edges:
    print(key)

print(f"\nNot found edge keys ({len(not_found_edges)}):")
for key in not_found_edges:
    print(key)

