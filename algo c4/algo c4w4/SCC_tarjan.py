import sys
import time




def tarjan(g:dict, n:int)->list:
    
    

    onstack = {}
    disc = {}
    low = {}

    stack = []
    cycles = []

    
   
    ftime=0

    def dfs(g:dict[int:list], ftime, i:int):
        
        
        stack.append(i)
        onstack[i] = True

        disc[i] = ftime
        low[i] = ftime
        ftime+=1

        for j in g.get(i,[]):

            if disc.get(j,-1)==-1:
                ftime = dfs(g, ftime, j)

                low[i] = min(low.get(j,float("inf")),low.get(i,float("inf")))
                
            
            elif onstack[j]:
                low[i] = min(disc.get(j,float("inf")),low.get(i,float("inf")))


        if disc[i] == low[i]:
            s = None
            cycle = []
            while s != i  :      
                
                s = stack.pop()
                onstack[s] = False
                cycle.append(s)
            cycles.append(cycle)

        return ftime
    
       



    for i in g.keys():
        if disc.get(i,-1)==-1:
            ftime = dfs(g, ftime, i)
           
    return cycles







