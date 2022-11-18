#task 2
#Graph traversal using BFS

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
        m_dic[int(j[1])] += [int(j[0])]
        # print(j[0],j[1])
    # print(m_dic)

    def bfs(done_lst, m_dic):
        q_lst = [1]
        s = ""
        while q_lst:
            m = q_lst.pop(0) 
            s += str(m) + " "

            for edges in m_dic[m]:
                if edges not in done_lst:
                    done_lst.append(edges)
                    q_lst.append(edges)

        return s
    done_lst = [1] # as we are starting from 1
    return (bfs(done_lst, m_dic))



with open('input2_1.txt', 'r') as file_in2_1:
    add = function(file_in2_1)
    with open('output2_1.txt', 'w') as file_out2_1:
        file_out2_1.write(add)

with open('input2_2.txt', 'r') as file_in2_2:
    add2 = function(file_in2_2)
    with open('output2_2.txt', 'w') as file_out2_2:
        file_out2_2.write(add2)

with open('input2_3.txt', 'r') as file_in2_3:
    add3 = function(file_in2_3)
    with open('output2_3.txt', 'w') as file_out2_3:
        file_out2_3.write(add3)

with open('input2_4.txt', 'r') as file_in2_4:
    add4 = function(file_in2_4)
    with open('output2_4.txt', 'w') as file_out2_4:
        file_out2_4.write(add4)