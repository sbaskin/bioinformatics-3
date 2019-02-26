import re
import sys

def read_pairs_string_reconstruction(k,d, read_pairs):
    directed_graph = create_directed_graph(read_pairs)
    path = find_eulerian_path(directed_graph)
    string = reconstruct_string(path, d)
    return string
    

def create_directed_graph(read_pairs):
    directed_graph = {}
    for pair1, pair2 in read_pairs:
        prefix = (pair1[:len(pair1) -1], pair2[:len(pair2) -1])
        suffix = (pair1[1:], pair2[1:])
        if prefix in directed_graph:
            directed_graph[prefix].append(suffix)
        else:
            directed_graph[prefix] = [suffix]
    return directed_graph

def create_read_pair_tuples(read_pair_strings):
    read_pair_tuples = []
    pattern = re.compile(r'\w+')
    for read_pair in read_pair_strings:
        kmers = pattern.findall(read_pair)
        read_pair_tuple = (kmers[0], kmers[1])
        read_pair_tuples.append(read_pair_tuple)
    return read_pair_tuples

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

def reconstruct_string(path, d):
    string = None
    ending = ""
    for i, read_pair in enumerate(path):
        if not string:
            string = read_pair[0]
        else:
            string += read_pair[0][len(read_pair[0]) - 1]
        beg = len(path) - (len(path) + 2*len(read_pair[0]) + d - len(path) - len(read_pair[0]) + 2)
        if i > beg:
            ending += read_pair[1][len(read_pair[1]) - 1]
    return string + ending


k = 3
d = 1
read_pairs = [
    "ACC|ATA",
    "ACT|ATT",
    "ATA|TGA",
    "ATT|TGA",
    "CAC|GAT",
    "CCG|TAC",
    "CGA|ACT",
    "CTG|AGC",
    "CTG|TTC",
    "GAA|CTT",
    "GAT|CTG",
    "GAT|CTG",
    "TAC|GAT",
    "TCT|AAG",
    "TGA|GCT",
    "TGA|TCT",
    "TTC|GAA"
]

sys.setrecursionlimit(10000)
#f = open('C:/Users/Shane/Downloads/dataset_204_15 (3).txt')

#numbers = f.readline()
#pattern = re.compile(r'\d+')
#numbers = pattern.findall(numbers)
#k = int(numbers[0])
#d = int(numbers[1])

#lines = f.readlines()
#l = [line.strip() for line in lines]



read_pairs = create_read_pair_tuples(read_pairs)
string = read_pairs_string_reconstruction(k, d, read_pairs)
print(string)