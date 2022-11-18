#task 1A
def function(f):
    input = f.read().split('\n')
    v, e = map(int, input[0].strip().split(' '))
    direction = [input[i].strip().split(' ') for i in range(1,e+1)]
    # print(input)
    # print(v, e)
    # print(direction)
    matrix = [[0 for i in range(v+1)] for j in range(v+1)]
    # print(matrix)
    for i in direction:
        matrix[int(i[0])][int(i[1])] = int(i[2])
    # print('After directed: ',matrix)
    s = ''
    for i in matrix:
        b = ''
        for j in i:
            b += str(j) + ' '
        s += b + '\n'

    return s

with open('input1a_1.txt', 'r') as file_in1a_1:
    s = function(file_in1a_1)
    with open('output1a_1.txt', 'w') as file_out1a_1:
        file_out1a_1.write(s)

with open('input1a_2.txt', 'r') as file_in1a_2:
    s = function(file_in1a_2)
    with open('output1a_2.txt', 'w') as file_out1a_2:
        file_out1a_2.write(s)