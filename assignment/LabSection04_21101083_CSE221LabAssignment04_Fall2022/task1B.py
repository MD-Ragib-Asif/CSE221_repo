#task 1B
def function(f):
    input = f.read().split('\n')
    v, e = map(int, input[0].strip().split(' '))
    direction = [input[i].strip().split(' ') for i in range(1,e+1)]
    # print(input)
    # print(v, e)
    # print(direction)
    
    m_dic = {}
    for i in range(v+1):
        m_dic[i] = []

    # print(m_dic)
    for i in direction:
        m_dic[int(i[0])] += [(int(i[1]), int(i[2]))]
    # print('After entering value: ', m_dic)
            
    s = ''
    for k,v in m_dic.items():
        b = ''
        for j in v:
            b += str(j) + ' '
        s += str(k) + ' : ' + b + '\n'

    return s


with open('input1b_1.txt', 'r') as file_in1b_1:
    s = function(file_in1b_1)
    with open('output1b_1.txt', 'w') as file_out1b_1:
        file_out1b_1.write(s)

with open('input1b_2.txt', 'r') as file_in1b_2:
    s = function(file_in1b_2)
    with open('output1b_2.txt', 'w') as file_out1b_2:
        file_out1b_2.write(s)

with open('input1b_3.txt', 'r') as file_in1b_3:
    s = function(file_in1b_3)
    with open('output1b_3.txt', 'w') as file_out1b_3:
        file_out1b_3.write(s)
