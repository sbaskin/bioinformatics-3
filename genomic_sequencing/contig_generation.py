


def get_next_start_index(directed_graph):
    for node in directed_graph:
        if directed_graph[node]:
            return node

def create_contig_from_path(cycle):
    contig = None
    for node in cycle:
        if not contig:
            contig = node
        else:
            contig += node[len(node)-1]
    return contig

def create_directed_graph(kmers):
    directed_graph = {}
    for kmer in kmers:
        suffix = kmer[1:]
        prefix = kmer[:len(kmer) -1]
        if prefix in directed_graph:
            directed_graph[prefix].append(suffix)
        else:
            directed_graph[prefix] = [suffix]
    return directed_graph


def maximal_non_branching_paths(directed_graph):
    paths = []
    for v in directed_graph:
        if not is_one_in_one_out(v, directed_graph):
            if number_of_out_edges(v, directed_graph) > 0:
                for w in directed_graph[v]:
                    non_branching_path = [v, w]
                    while is_one_in_one_out(w, directed_graph):
                        non_branching_path.append(directed_graph[w][0])
                        w = directed_graph[w][0]
                    paths.append(non_branching_path)
    return paths

def is_one_in_one_out(node, directed_graph):
    in_edges = number_of_in_edges(node, directed_graph)
    out_edges = number_of_out_edges(node, directed_graph)
    if in_edges == 1 and out_edges == 1:
        return True
    return False

def number_of_in_edges(node, directed_graph):
    count = 0
    for n1 in directed_graph:
        for n2 in directed_graph[n1]:
            if n2 == node:
                count += 1
    return count

def number_of_out_edges(node, directed_graph):
    if node in directed_graph:
        return len(directed_graph[node])
    return 0

kmers = [
    "ATG",
    "ATG",
    "TGT",
    "TGG",
    "CAT",
    "GGA",
    "GAT",
    "AGA"
]

#contigs = generate_contigs(kmers)
#print(contigs)

f = open('C:/Users/Shane/Downloads/dataset_205_5.txt')

kmers = f.readlines()
kmers = [kmer.strip() for kmer in kmers]

directed_graph = create_directed_graph(kmers)
paths = maximal_non_branching_paths(directed_graph)
contigs = [create_contig_from_path(path) for path in paths]

output = ""
for contig in contigs:
    output += contig + ' '
print(output)