def function(target, road, start, lines):
    lst_v = []
    check = []
    for i in range(1, target+1):
        lst_v += [i]

    for i in range(start+1, start+road+1):
        a, b, c = lines[i].split(" ")
        check += [[int(a), int(b), int(c)]]

    adj_lst = {}
    for j in lst_v:
        adj_lst[j] = []
        for i in check:
            a, b, c = i
            if j == a:
                if b not in adj_lst[j]:
                    adj_lst[j] +=[b]
            elif j == b:
                if a not in adj_lst[j]:
                    adj_lst[j] +=[a]

    adjust = {}
    for k in lst_v:
        adjust[k] = [float('inf'), None, False] # [distance, predecessor, visited]

    # print(lst_v)
    # print(check)
    # print(adj_lst)

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
            elif check[i][0] == neighbour and check[i][1] == u:
                return check[i][2]

    def dijkstra(graph, src, dest, adjust, lst_v, check):
        if src not in graph:
            raise TypeError('The root of the shortest path tree cannot be found')
        if dest not in graph:
            raise TypeError('The target of the shortest path cannot be found')
        
        adjust[src][0], adjust[src][2] = 0, True
        while lst_v:
            u = check_min(adjust, lst_v)
            adjust[u][2] = True
            for neighbours in graph[u]:
                alt_dist = adjust[u][0] + distance(check, u, neighbours)
                if alt_dist < adjust[neighbours][0]:
                    adjust[neighbours][0] = alt_dist
                    adjust[neighbours][1] = u
            lst_v.remove(u)

        return adjust[dest][1], adjust

    
    p_lst = [target]
    parent, dic = dijkstra(adj_lst, 1, target, adjust, lst_v, check)
    if parent != None:
        p_lst += [parent]

    rem = parent
    for k, v in dic.items():
        if k == rem:
            if v[1] != None:
                p_lst += [v[1]]
                rem = v[1]

    return p_lst[::-1]

with open("input2.txt", "r") as filein_3:
    with open('output3.txt', 'w') as fileout_3:
        lines = filein_3.read().split("\n")
        for i in range(len(lines)):
            if len(lines[i].split(" ")) == 2:
                a, b = map(int, lines[i].split(" "))
                lst = function(a, b, i, lines)
                for i in lst:
                    fileout_3.write(str(i) + " ")
                fileout_3.write("\n")
            else:
                continue
