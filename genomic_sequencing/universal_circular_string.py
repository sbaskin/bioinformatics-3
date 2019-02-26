

def solve_universal_circular_string(k):
    strings = get_all_strings(k)
    directed_graph = create_directed_graph(strings)
    cycle = solve_eulerian_cycle(directed_graph)
    print(cycle)
    cycle = cycle[:len(cycle)-3]
    return reconstruct_string(cycle)

def get_all_strings(k):
    strings = get_all_strings_helper(0, k, [''])
    return strings

def get_all_strings_helper(i, k, strings):
    if i == k:
        return strings
    all_strings = []
    for binary in ['0', '1']: 
        new_strings = []
        for string in strings:
            new_strings.append(string + binary)
        new_strings = get_all_strings_helper(i+1, k, new_strings)
        all_strings += new_strings
    return all_strings

def create_directed_graph(strings):
    directed_graph = {}
    for string in strings:
        prefix = string[:len(string)-1]
        suffix = string[1:]
        if prefix in directed_graph:
            directed_graph[prefix].append(suffix)
        else:
            directed_graph[prefix] = [suffix]
    return directed_graph

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

def reconstruct_string(cycle):
    text = None
    for string in cycle:
        if not text:
            text = string
        else:
            text += string[len(string) - 1]
    return text

string = solve_universal_circular_string(9)
print(string, len(string))