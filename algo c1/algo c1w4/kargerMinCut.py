import random 
import time
import copy

class nodes:
    def __init__(self,name,neighbors):
        self.name = name    
        self.neighbors = neighbors if len(neighbors)!=0 else []




def read_graph(filename):

    f = open(filename, "r")
    l = list( f.readlines())


    g={}
    for i in range(len(l)):

        tmp = l[i].split('\t')
        tmp = tmp[1:-1]
        g[i]=[int(x)-1 for x in tmp ]


    # print(" ==================================================================" )
    # print( g[0])
    # print(type( g[0]),end="\n")
    # print(type( g[0][0]),end="\n")
    # print(" ==================================================================" )

    return g



def choose_edge(g):
    a = random.choice(list(g.keys()))
    b = random.choice(g[a])
    if len(g[b]) > len(g[a]):
        tmp = a
        a = b
        b = tmp
    return a,b





def karger_Min_Cut(g:dict[list]):

    if len(list(g.keys())) <= 2:
        return len(g[list(g.keys())[0]]) 
    
    a,b = choose_edge(g)

    for i in g[b]:
        while b in g[i]:
            g[i].remove(b)
            g[i].append(a)


                
    g[a].extend(g[b])

    del g[b]

    while b in g[a]:
        g[a].remove(b) 


    while  a in g[a] :
        g[a].remove(a)

    return karger_Min_Cut(g)

    

def kargerMinCut(g,n):
    mincuts =  9999999999999999999999999
   
    for i in range(n):
        g_ = copy.deepcopy(g)
        # random.seed(i*2+1)

        cuts =  karger_Min_Cut(g_)

        mincuts = min(mincuts,cuts)
        del g_
    return mincuts




g = read_graph("kargerMinCut.txt")
n = len(list(g.keys()))
s = time.time()
print("min cuts = ",kargerMinCut(g,n))
e = time.time()
print("run time =",e-s, " seconds", )

