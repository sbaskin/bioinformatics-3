import sys

def solve_string_reconstruction(kmers):
    directed_graph = create_directed_graph(kmers)
    path = find_eulerian_path(directed_graph)
    text = recreate_string(path)
    return text


def create_directed_graph(kmers):
    directed_graph = {}
    for kmer in kmers:
        prefix = kmer[:len(kmer)-1]
        suffix = kmer[1:]
        if prefix in directed_graph:
            directed_graph[prefix].append(suffix)
        else:
            directed_graph[prefix] = [suffix]
    return directed_graph

def find_eulerian_path(directed_graph):
    start_nodes = find_all_possible_start_nodes(directed_graph)
    path = []
    for start_node in start_nodes:
        path = solve_eulerian_cycle(directed_graph.copy(), start_node)
        if path:
            break
    return path

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

def recreate_string(path):
    text = None
    for kmer in path:
        if not text:
            text = kmer
        else:
            text += kmer[len(kmer) - 1]
    return text
        

k = [
    "AAAT",
    "AATG",
    "ACCC",
    "ACGC",
    "ATAC",
    "ATCA",
    "ATGC",
    "CAAA",
    "CACC",
    "CATA",
    "CATC",
    "CCAG",
    "CCCA",
    "CGCT",
    "CTCA",
    "GCAT",
    "GCTC",
    "TACG",
    "TCAC",
    "TCAT",
    "TGCA"
]

sys.setrecursionlimit(3000)

#f = open('C:/Users/Shane/Downloads/dataset_203_7.txt')
#discard = f.readline()
#kmers = f.readlines()
#kmers = [k.strip() for k in kmers]

text = solve_string_reconstruction(k)
print(text)