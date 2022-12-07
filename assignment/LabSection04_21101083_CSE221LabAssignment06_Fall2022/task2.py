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
    check = []
    for k in m_lst:
        if k not in n_lst:
            check.append(k)
    # print(check)
    n_lst.append(check[0])
    idx2 = 0
    for l in range(1, len(check)):
        if check[idx2][0] <= check[l][1]:
            n_lst.append(check[l])
            idx2 = l

    return len(n_lst)


with open("input2_1.txt", 'r') as filein2_1:
    with open("output2_1.txt", 'w') as fileout2_1:
        a = function(filein2_1)
        fileout2_1.write(str(a))

with open("input2_2.txt", 'r') as filein2_2:
    with open("output2_2.txt", 'w') as fileout2_2:
        a2 = function(filein2_2)
        fileout2_2.write(str(a2))