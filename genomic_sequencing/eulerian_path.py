import re
import sys

def find_eulerian_path(directed_graph):
    start_nodes = find_all_possible_start_nodes(directed_graph)
    cycle = []
    for start_node in start_nodes:
        cycle = solve_eulerian_cycle(directed_graph.copy(), start_node)
        if cycle:
            break
    return cycle

def find_all_possible_start_nodes(directed_graph):
    start_nodes = []
    for node in directed_graph:
        out_nodes = len(directed_graph[node])
        in_nodes = count_in_nodes(directed_graph, node)
        if out_nodes > in_nodes:
            start_nodes.append(node)
    return start_nodes

def count_in_nodes(directed_graph, node):
    in_nodes = 0
    for n in directed_graph:
        if node in directed_graph[n]:
            in_nodes += 1
    return in_nodes

def solve_eulerian_cycle(directed_graph, start_node):
    cycle = []
    solve_eulerian_cycle_helper(start_node, directed_graph, cycle)
    if has_unused_edges(directed_graph):
        return
    cycle.reverse()
    return cycle

def has_unused_edges(directed_graph):
    for node in directed_graph:
        if directed_graph[node]:
            return True
    return False

def solve_eulerian_cycle_helper(node_index, directed_graph, cycle):
    if node_index in directed_graph:
        while directed_graph[node_index]:
            next_node_index = directed_graph[node_index].pop()
            solve_eulerian_cycle_helper(next_node_index, directed_graph, cycle)
    cycle.append(node_index)

def convert_input_to_directed_graph(lines):
    directed_graph = {}
    pattern = re.compile(r'\d+')
    for line in lines:
        numbers = pattern.findall(line)
        value = numbers[0]
        neighbors = numbers[1:]
        directed_graph[value] = neighbors
    return directed_graph

def convert_eulerian_cycle_to_output_format(eulerian_cycle):
    output = ''
    for i, node in enumerate(eulerian_cycle):
        if i:
            output += '->'
        output += node
    return output

lines = [
    "0 -> 2",
    "1 -> 3",
    "2 -> 1",
    "3 -> 0,4",
    "6 -> 3,7",
    "7 -> 8",
    "8 -> 9",
    "9 -> 6"
]

f = open('C:/Users/Shane/Downloads/dataset_203_6 (2).txt')

lines = f.readlines()
l = [line.strip() for line in lines]

directed_graph = convert_input_to_directed_graph(l)
eulerian_cycle = find_eulerian_path(directed_graph)
output = convert_eulerian_cycle_to_output_format(eulerian_cycle)

print(output)