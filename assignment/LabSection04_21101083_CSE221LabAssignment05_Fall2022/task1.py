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