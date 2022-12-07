def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def function(f):
    inputs = f.read().split("\n")
    # print(inputs)
    m_lst = []
    for i in range(1, len(inputs)):
        a, b = map(int, inputs[i].split(" "))
        m_lst.append([b, a])
        
    # print(m_lst)
    insertion_sort(m_lst)
    # print(m_lst)
    n_lst = [m_lst[0]]
    idx = 0
    for j in range(1, len(m_lst)):
        if m_lst[idx][0] <= m_lst[j][1]:
            n_lst.append(m_lst[j])
            idx = j
    # print(n_lst)
    s = str(len(n_lst)) + '\n'
    for i in n_lst:
        s += str(i[1]) + ' ' + str(i[0]) + '\n'
    return s

with open("input1_1.txt", 'r') as filein1_1:
    with open("output1_1.txt", 'w') as fileout1_1:
        a = function(filein1_1)
        fileout1_1.write(a)


with open("input1_2.txt", 'r') as filein1_2:
    with open("output1_2.txt", 'w') as fileout1_2:
        a2 = function(filein1_2)
        fileout1_2.write(a2)
        
