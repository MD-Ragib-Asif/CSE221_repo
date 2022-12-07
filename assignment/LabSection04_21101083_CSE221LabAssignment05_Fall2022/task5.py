from math import inf


with open('input5.txt','r') as f:
    inputs = f.read()

inputs = inputs.split('\n')
# test_cases = int(inputs[0])
sources = []


g_count = int(inputs.pop(0))
graph = [{} for _ in range(g_count)] 

# print(graph,g_count)


for x in range(g_count):
    t = inputs.pop(0).split(' ')

    for y in range(int(t[-1])):



        a,b,c = map(int, inputs.pop(0).split(' '))

        if a not in graph[x].keys():
            graph[x][a] = [[b,c]]
        
        else:
            graph[x][a] += [[b,c]]

    sources += [int(inputs.pop(0))]



def dijkstra(graph,source=1):

    if len(graph) == 0 : return [0,0],[0,source]
    list1 = []
    for x,y in graph.items(): list1 += [x,y[0][0]]
    length =max(list1)+1               # (length + 1) because the graph vertexes started from 1 not 0   
    dist = [0]*length
    prev = [None]*length
    visited = [0]*length

    dist[source]=0      
    Q = []


    
    for v in graph.keys():
        if v != 0:
            if source != v:
                dist[v] = -1
                prev[v] = None
 
            Q.append((dist[v],v))
            visited[v] = False

    while len(Q)>0:
 

        Q.sort(reverse=True)
        u = Q.pop()[-1]
        if visited[u]:
            continue
        visited[u] = True
        if u not in graph.keys():
            continue
        for neighbour in graph[u]:
            alt = max(dist[u] ,dist[u]+ neighbour[1])
            if alt > dist[neighbour[0]] :
                dist[neighbour[0]] =  alt
                prev[neighbour[0]] = u 
                Q.append((dist[neighbour[0]],neighbour[0]))
    return dist,prev
s=''
for x in range(len(graph)):
    s += str(dijkstra(graph[x],sources[x])[0][1:])+'\n'
with open('output5.txt','w') as f:
    f.write(s)

