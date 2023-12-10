import os.path as path
from union import UnionFind
project_dir = path.dirname (path.abspath (__file__))

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n= int(lines[0])
    lines = lines[1:]

    edges = []
    for line in lines:
        l = line.split()
        v1 = int(l[0])-1
        v2 = int(l[1])-1
        w = int(l[2])
        edges.append([v1,v2,w])
        
    edges.sort(key=lambda x: x[2])
    return edges, n



def kruskal(edges, n):

    setX = UnionFind(n)
    T=[]
    
    for edge in edges:
        v,u,w = edge

        
        if setX.find(v) == setX.find(u):
            continue
        else:
            setX.union(u,v) 
            T.append(edge)  
            n-=1



        

    return T





edges, n = read_file(project_dir+'\\clustering1.txt')
K=4
T = kruskal(edges, n)
T.reverse()
cost = T[:K-1]
print (cost)