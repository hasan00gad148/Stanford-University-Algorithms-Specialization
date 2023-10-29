import os.path as path
from itertools import combinations as comb
from union import UnionFind
project_dir = path.dirname (path.abspath (__file__))

def read_file(filename):
    file = open(filename,'r')
    nodes = {}
    names = {}
    lines = file.readlines()
    n,n_bits = list(map(int, lines[0].split()))
    lines = lines[1:]
    es = []
    for i,line in enumerate(lines):
        line = "".join(line[:-1].split())   
        num = int(line,2)
        nodes[i] = num
        if names.get(num, None) is  None:
            names[num]=[i,]
        else:
            names[num].append(i)
            


    return nodes,names,n, n_bits




def getDef1AndDef2Edges(nodes, n, n_bits):

    edges1={}
    edges2={}


    l = list(range(n_bits))
    l = list(comb(l,2))

    for i,n in nodes.items():
        for b in range(n_bits):
            mask = n ^ (1 << b)
            if edges1.get(i, None)!=None:            
                edges1[i].append(mask)
            else:
              edges1[i] = [mask,]

        for b1,b2 in l:
            mask = n ^ (1 << b1)
            mask = mask ^ (1 << b2)
            if edges2.get(i, None)!=None:
                edges2[i].append(mask)   
            else:
                edges2[i] = [mask,]
                   

    return edges1,edges2          



def getEdges(nodes, names, n, n_bits):
    edges1, edges2 = getDef1AndDef2Edges(nodes, n, n_bits)
    edges= []

    keys =  list(nodes.keys())
    for k in range(len(keys)):
        for j in range(k+1,len(keys)):
            if nodes[k] == nodes[j]:
                edges.append([j,k,0])
        

    for n in edges1.keys():
        for mask in edges1[n]:
            i = names.get(mask, None)
            if i != None:
                for j in i:
                    edge =[n,j,1]
                    edges.append(edge)
    for n in edges2.keys():
        for mask in edges2[n]:
            i = names.get(n, None)
            if i != None:
                for j in i:
                    edge =[n,j,2]
                    edges.append(edge)
    
    return edges




 



def kruskal(edges,n):

    setX = UnionFind(n)
    T=[]

    for edge in edges:
        v,u,w = edge

        
        if setX.find(v) == setX.find(u):
            continue
        else:
            setX.union(u,v) 
            T.append(edge)  


        

    return T,setX


nodes, names, n, n_bits = read_file(project_dir+'\\clustering_big.txt')
edges = getEdges(nodes, names, n, n_bits)

T,X=kruskal(edges, n)



s = set()
for i in range(200000):
    p = X.find(i)
    if p in s:
        continue
    s.add(p)

print(len(edges),len(T),len(s))