import re
import sys

def solve_eulerian_cycle(directed_graph):
    cycle = []
    node_index = list(directed_graph.keys())[0]
    solve_eulerian_cycle_helper(node_index, directed_graph, cycle)
    cycle.reverse()
    return cycle

def solve_eulerian_cycle_helper(node_index, directed_graph, cycle):
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
    "0 -> 3",
    "1 -> 0",
    "2 -> 1,6",
    "3 -> 2",
    "4 -> 2",
    "5 -> 4",
    "6 -> 5,8",
    "7 -> 9",
    "8 -> 7",
    "9 -> 6"
]

f = open('C:/Users/Shane/Downloads/dataset_203_6.txt')

lines = f.readlines()
lines = [line.strip() for line in lines]

directed_graph = convert_input_to_directed_graph(lines)
eulerian_cycle = solve_eulerian_cycle(directed_graph)
output = convert_eulerian_cycle_to_output_format(eulerian_cycle)

print(output)
