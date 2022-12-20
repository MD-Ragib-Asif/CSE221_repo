###sort
def ins_sort(arr):
    for num in range(1,len(arr)):
        t_val=arr[num]
        temp=num-1
        while temp>=0 and t_val>arr[temp]:
            arr[temp+1]=arr[temp]
            temp-=1
        arr[temp+1]=t_val

###reverse_sort
def insertionRev(lst):
    for i in range(1,len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key > lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key

###merge_sort
def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i,j,k = 0,0,0 


        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

###graph_adj_matrix
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


###Graph traversal using BFS
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

###dijkstra
with open('input1.txt', 'r') as filein_1:
    lines = filein_1.read().split("\n")
    # v, t = map(int, lines[0].strip().split(" "))
    # print(v, t)
    # print(lines)
    lst_v = []
    check = []
    for i in range(len(lines)):
        a, b, c = lines[i].split(" ")
        check += [[a, b, int(c)]]
        if a not in lst_v:
            lst_v.append(a)
        if b not in lst_v:
            lst_v.append(b)
    adj_lst = {}
    for j in lst_v:
        for i in range(len(lines)):
            a, b, c = lines[i].split(" ")
            if j == a:
                if j in adj_lst:
                    adj_lst[j]+=[b]
                else:
                    adj_lst[j] = [b]
        if j not in adj_lst:
            adj_lst[j] = []
    # print(lst_v)
    # print(adj_lst)
    # print(check)
    adjust = {}
    for k in lst_v:
        adjust[k] = [float('inf'), None, False] # [distance, predecessor, visited]
    # print(adjust)
    def check_min(check, lst_v):
        min = 99999999999999999999999999999
        key = None
        for i in lst_v:
            if check[i][0] < min:
                min = check[i][0]
                key = i
        return key
    def distance(check, u, neighbour):
        for i in range(len(check)):
            if check[i][0] == u and check[i][1] == neighbour:
                return check[i][2]
    def dijkstra(graph, src, dest, adjust, lst_v, check):
        if src not in graph:
            raise TypeError('The root of the shortest path tree cannot be found')
        if dest not in graph:
            raise TypeError('The target of the shortest path cannot be found')
        
        adjust[src][0], adjust[src][2] = 0, True
        # print(adjust)
        while lst_v:
            u = check_min(adjust, lst_v)
            # print(u)
            # if adjust[u][2]:
            #     continue
            adjust[u][2] = True
            for neighbours in graph[u]:
                alt_dist = adjust[u][0] + distance(check, u, neighbours)
                if alt_dist < adjust[neighbours][0]:
                    adjust[neighbours][0] = alt_dist
                    adjust[neighbours][1] = u
            lst_v.remove(u)
        print(adjust)
        print("Distance: ",adjust[dest][0])
        print("Parent of ", dest, "is: ", adjust[dest][1])
    dijkstra(adj_lst, 'Motijheel', 'MOGHBAZAR', adjust, lst_v, check)

###