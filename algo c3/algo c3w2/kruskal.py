import os.path as path
from union import UnionFind
project_dir = path.dirname (path.abspath (__file__))

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n,m = list(map(int, lines[0].split()))
    lines = lines[1:]

    edges = []
    for line in lines:
        l = line.split()
        v1 = int(l[0])-1
        v2 = int(l[1])-1
        w = int(l[2])
        edges.append([v1,v2,w])
        
    edges.sort(key=lambda x: x[2])
    return edges, n, m



def kruskal(edges, n, m):

    visited = [False]*n
    i = 0
    setX = UnionFind(n)

    cost = 0
    
    for edge in edges:

        v,u,w = edge
        if setX.find(v) == setX.find(u):
            continue
        else:
            setX.union(u,v)
            cost += w


        

    return cost





edges, n, m = read_file(project_dir+'\\edges.txt')

cost = kruskal(edges, n, m)

print (cost)