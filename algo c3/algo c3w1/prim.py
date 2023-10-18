import os.path as path
from minHeap import MinHeap
project_dir = path.dirname (path.abspath (__file__))

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n,m = list(map(int, lines[0].split()))
    lines = lines[1:]

    g = [None] * n
    for line in lines:
        l = line.split()
        v1 = int(l[0])-1
        v2 = int(l[1])-1
        w = int(l[2])

        if g[v1] :
            g[v1].append([v2,w])
        else :
            g[v1] =[[v2,w],]

        if g[v2] :
            g[v2].append([v1,w])
        else :
            g[v2] =[[v1,w],]




        

    return g, n, m



def prim(g, n, m):


    heap =  MinHeap()
    cost = 0
    visited = [False]*n



    v = 151
            
    visited[v]= True

    for e in g[v]:
        if not visited[e[0]]:
            heap.add([e[0],v,e[1]])


    while  heap.size:

        
        # if visited[v]:
        #     continue
        e = heap.extractMin()
        v = e[0]
        if not visited[v]:
            cost += e[2]
            visited[v]= True

            for e in g[v]:
                if not visited[e[0]]:
                    heap.add([e[0],v,e[1]])
        

        







    return cost





g, n, m = read_file(project_dir+'\\edges.txt')

cost = prim(g, n, m)

print (cost)