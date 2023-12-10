import os.path as path
from itertools import combinations as comb
from union import UnionFind
project_dir = path.dirname (path.abspath (__file__))

def read_file(filename):
    file = open(filename,'r')
    nodes = {}
    lines = file.readlines()
    n,n_bits = list(map(int, lines[0].split()))
    lines = lines[1:]
    "c is the number of repeated nodes"

    for i,line in enumerate(lines):
        line = "".join(line[:-1].split())
        num = int(line,2)
        if nodes.get(num,None) is None:
            nodes[num] = i



    return nodes, n, n_bits




def getDef1AndDef2Edges(nodes, n, n_bits):

    edges1={}
    edges2={}


    l = list(range(n_bits))
    l = list(comb(l,2))

    for n in nodes.keys():
        for b in range(n_bits):
            mask = n ^ (1 << b)
            if edges1.get(n, None)!=None:            
                edges1[n].append(mask)
            else:
              edges1[n] = [mask,]

        for b1,b2 in l:
            mask = n ^ (1 << b1)
            mask = mask ^ (1 << b2)
            if edges2.get(n, None)!=None:
                edges2[n].append(mask)   
            else:
                edges2[n] = [mask,]
                   

    return edges1,edges2          



def getEdges(nodes, n, n_bits):
    edges1, edges2 = getDef1AndDef2Edges(nodes, n, n_bits)
    edges= []
   
    for n in edges1.keys():
        for mask in edges1[n]:
            if nodes.get(mask, None):
                edge =[n,mask,1]
                edges.append(edge)
    for n in edges2.keys():
        for mask in edges2[n]:
            if nodes.get(mask, None):
                edge =[n,mask,2]
                edges.append(edge)


    return edges




 



def kruskal(edges,nodes,n):

    setX = UnionFind(n)
    T=[]

    for edge in edges:
        v,u,w = edge
        v = nodes[v]
        u = nodes[u]
        
        if setX.find(v) == setX.find(u):
            continue
        else:
            setX.union(u,v) 
            T.append(edge)  


        

    return T


nodes, n, n_bits, = read_file(project_dir+'\\clustering_big.txt')
edges = getEdges(nodes, n, n_bits)

T = kruskal(edges, nodes, len(edges))

print(len(T),len(edges),len(nodes))
print ("the answer is ",len(nodes)-len(T))

"""

"""