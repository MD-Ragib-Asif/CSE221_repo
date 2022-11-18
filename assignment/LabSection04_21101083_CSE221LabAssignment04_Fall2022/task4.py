#task 4

def function(f):
    input = f.read().split('\n')
    v, e = map(int, input[0].strip().split(' '))
    direction = [input[i].strip().split(' ') for i in range(1,e+1)]
    # print(input)
    # print(v, e)
    # print(direction)
    
    m_dic = {}
    for i in range(1,v+1):
        m_dic[i] = []

    for j in direction:
        m_dic[int(j[0])] += [int(j[1])]
        # print(j[0],j[1])
    # print(m_dic)
    graph_lst = [v for k,v in m_dic.items()]

    def dfs(done_lst, m_dic):
        q_lst = [1]
        nlst = []

        while q_lst:
            m = q_lst.pop() 
            nlst.append(m)

            for edges in m_dic[m]:
                if edges not in done_lst:
                    done_lst.append(edges)
                    q_lst.append(edges)

        return nlst
    done_lst = [1] # as we are starting from 1
    return (dfs(done_lst, m_dic), v, graph_lst)

# cass CheckCycle:
def cycle(arr, v, graph_lst):
    time = 0
    visited = [False] * (v+1)
    start_time = [0] * (v+1)
    end_time = [0] * (v+1)
    for node in range(1, (v+1)):
        if not visited[node]:
            visited[node] = True
            arr.append(node)
            start_time[node] = time
            time += 1
            for neighbour in graph_lst[node-1]:
                if start_time[node] > start_time[neighbour] and end_time[node] < end_time[neighbour]:
                    return True
                end_time[node] = time
                time += 1
    return False

with open('input4_1.txt', 'r') as file_in4_1:
    arr, v, graph_lst = function(file_in4_1)
    a = cycle(arr, v, graph_lst)
    with open('output4_1.txt', 'w') as file_out4_1:
        if a == False:
            file_out4_1.write('No')
        else:
            file_out4_1.write("Yes")

with open('input4_2.txt', 'r') as file_in4_2:
    arr2, v2, graph_lst2 = function(file_in4_2)
    a2 = cycle(arr2, v2, graph_lst2)
    with open('output4_2.txt', 'w') as file_out4_2:
        if a2 == False:
            file_out4_2.write('No')
        else:
            file_out4_2.write("Yes")

with open('input4_3.txt', 'r') as file_in4_3:
    arr3, v3, graph_lst3 = function(file_in4_3)
    a3 = cycle(arr3, v3, graph_lst3)
    with open('output4_3.txt', 'w') as file_out4_3:
        if a3 == False:
            file_out4_3.write('No')
        else:
            file_out4_3.write("Yes")

with open('input4_4.txt', 'r') as file_in4_4:
    arr4, v4, graph_lst4 = function(file_in4_4)
    a4 = cycle(arr4, v4, graph_lst4)
    with open('output4_4.txt', 'w') as file_out4_4:
        if a4 == False:
            file_out4_4.write('No')
        else:
            file_out4_4.write("Yes")

with open('input4_5.txt', 'r') as file_in4_5:
    arr5, v5, graph_lst5 = function(file_in4_5)
    a5 = cycle(arr5, v5, graph_lst5)
    with open('output4_5.txt', 'w') as file_out4_5:
        if a5 == False:
            file_out4_5.write('No')
        else:
            file_out4_5.write("Yes")




    