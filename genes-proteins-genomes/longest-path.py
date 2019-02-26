import math
def longest_path(node, path, value, end, dag):
    if node == end:
        return (path, value)
    elif node not in dag:
        return (path, -math.inf)

    solutions = []
    for child in dag[node]:
        childpath = path + '->{}'.format(child['node'])
        childvalue = value + child['weight']
        solution = longest_path(child['node'], childpath, childvalue, end, dag)
        solutions.append(solution)

    max_solution = None
    for solution in solutions:
        if not max_solution or solution[1] > max_solution[1]:
            max_solution = solution
    return max_solution


f = open('C:\\Users\\Shane\\Downloads\\dataset_245_7.txt')

start = f.readline().replace('\n', '')
end = f.readline().replace('\n', '')
edges = f.readlines()
dag = {}
for edge in edges:
    e = edge.replace('\n','')
    temp = e.split('->')
    temp2 = temp[1].split(':')
    node1 = temp[0]
    node2 = temp2[0]
    weight = int(temp2[1])
    element = {"node": node2, "weight": weight}
    if node1 in dag:
        dag[node1].append(element)
    else:
        dag[node1] = [element]

solution = longest_path(start, start, 0, end, dag)
print(solution[1])
print(solution[0])

