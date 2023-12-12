import sys
import time
sys.setrecursionlimit(2**20)

from SCC_tarjan import tarjan




def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    n = int(lines[0])
    lines = lines[1:]

    constraints = []
    for line in lines:
        constraints.append(list(map(int, line.split())))

    return constraints, n



def construct_graph(constraints,n):
    g = {}

    for x,y in constraints:
            if g.get(-x,None) is not None:
                g[-x].append(y)
            else:
                 g[-x] = [y,]
            

            if g.get(-y, None) is not None:
                g[-y].append(x)
            else:
                 g[-y] = [x,]

    return g


def SAT_2(g,n):
    cycles = tarjan(g,n+1)


    for cycle in cycles:
        s = set(cycle)
        for x in s:
              if -x in s:
                   return False


    return True
    
              
        







filenames = ["./2sat1.txt", "./2sat2.txt","./2sat3.txt","./2sat4.txt","./2sat5.txt","./2sat6.txt"]



for f in filenames:
    s= time.time()
    constraints, n = read_file(f)
    g = construct_graph(constraints,n)
    ans = SAT_2(g,n)
    e = time.time() 
    print(ans,e-s)
   