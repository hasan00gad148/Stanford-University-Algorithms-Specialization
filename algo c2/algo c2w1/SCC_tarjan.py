import sys
import time




def read_graph(filename):
    g={}

    file = open(filename, 'r')
    edges = file.readlines()
    n = -1
    for edge in edges:
        v1, v2 = list(map(lambda x : int(x)-1,edge.split(' ')[:2]))
        n = max(n,v1,v2)

        if v1 == v2:
            continue

        if len(g.get(v1,[])):
            g[v1].append(v2)

        else:
            g[v1]=[v2,]
           
        

    return g, n+1
    





    



def dfs(g:dict, n:int)->list:
    
    

    onstack = [False]*n
    disc = [-1]*n
    low = [-1]*n

    stack = []
    cycles = []

    
   
    ftime=0

    def _dfs(g:dict[int:list], ftime, i:int):
        
        
        stack.append(i)
        onstack[i] = True

        disc[i] = ftime
        low[i] = ftime
        ftime+=1

        for j in g.get(i,[]):

            if disc[j]==-1:
                ftime = _dfs(g, ftime, j)

                low[i] = min(low[j],low[i])
                
            
            elif onstack[j]:
                low[i] = min(disc[j], low[i])


        if disc[i] == low[i]:
            s = -100
            count = 0
            while s != i  :      
                
                s = stack.pop()
                onstack[s] = False
                count +=1
            cycles.append(count)

        return ftime
    
       



    for i in g.keys():
        if disc[i]==-1:
            ftime = _dfs(g, ftime, i)
           
    return cycles












g,  n = read_graph("./SCC.txt")
print(len(g),n,g[0],g[1],g[2])

print("recursion limit",sys.getrecursionlimit())
sys.setrecursionlimit(n*2)
print("recursion limit",sys.getrecursionlimit())

s= time.time()
l = dfs(g,n)
l.sort(reverse=True)
e = time.time()

print(l[:10])
print("run time=",e-s)