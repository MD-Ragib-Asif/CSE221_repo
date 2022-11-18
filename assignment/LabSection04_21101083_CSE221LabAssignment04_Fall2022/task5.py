def shortest_path(graph, s_node, e_node):
    lst = []
    queue = [[s_node]]

    if s_node == e_node:
        s = f"Time: 0 \nShortest Path: {s_node}"
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in lst:
            edges = graph[node]

        for neighbour in edges:
            new_path = list(path)
            new_path.append(neighbour)
            queue.append(new_path)

        if neighbour == e_node:
            s = f"Time: {len(new_path)-1} \n"
            s += "Shortest Path: {}".format(*new_path)
            return s

        lst.append(node)
    return f'Dose not exist'


def function(f):
    input = f.read().split('\n')
    v, e, t = map(int, input[0].strip().split(' '))
    direction = [input[i].strip().split(' ') for i in range(1,e+1)]
    # print(input)
    # print(v, e)
    # print(direction)
    
    m_dic = {}
    for i in range(1,v+1):
        m_dic[i] = []

    for j in direction:
        m_dic[int(j[0])] += [int(j[1])]
        m_dic[int(j[1])] += [int(j[0])]
        # print(j[0],j[1])
    # print(m_dic)
    return m_dic, t

with open("input5_1.txt", "r") as file_in5_1:
    graph, t = function(file_in5_1)
    add = shortest_path(graph, 1, t)
    with open("output5_1.txt", 'w') as file_out5_1:
        file_out5_1.write(add)

with open("input5_2.txt", "r") as file_in5_2:
    graph2, t2 = function(file_in5_2)
    add2 = shortest_path(graph2, 1, t2)
    with open("output5_2.txt", 'w') as file_out5_2:
        file_out5_2.write(add2)

with open("input5_3.txt", "r") as file_in5_3:
    graph3, t3 = function(file_in5_3)
    add3 = shortest_path(graph3, 1, t3)
    with open("output5_3.txt", 'w') as file_out5_3:
        file_out5_3.write(add3)

with open("input5_4.txt", "r") as file_in5_4:
    graph4, t4 = function(file_in5_4)
    add4 = shortest_path(graph4, 1, t4)
    with open("output5_4.txt", 'w') as file_out5_4:
        file_out5_4.write(add4)

with open("input5_5.txt", "r") as file_in5_5:
    graph5, t5 = function(file_in5_5)
    add5 = shortest_path(graph5, 1, t5)
    with open("output5_5.txt", 'w') as file_out5_5:
        file_out5_5.write(add5)