import sys
import time




def read_graph(filename):
    g={}
    grev = {}
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
           
        
        if len(grev.get(v2,[])):
            grev[v2].append(v1)

        else:
            grev[v2]=[v1,]


    return g, n+1, grev
        



def _dfs(g:dict[int:list],explored:list,fTime:int,fTimes:list,i:int)->int:

    explored[i] = True
    for j in g.get(i,[]):
        if not explored[j]:
            fTime = _dfs(g,explored,fTime,fTimes,j)

    fTimes[fTime] =i
    fTime += 1

    return fTime


def dfs(g:dict, n:int)->list:
    fTime = 0
    fTimes = [-1]*n
    explored = [False]*n

    for i in g.keys():
        if not explored[i]:
           fTime =_dfs(g,explored,fTime,fTimes,i)
           

    return fTimes






def _kosaraju(g:dict, explored:list,i:int)->int:
    
    
    explored[i] = True
    count = 0
    for j in g.get(i,[]):
        if not explored[j]:
            count += _kosaraju(g,explored,j)

    count += 1
    return count


def kosaraju(g:dict, n:int, grev)->dict:
    
    fTimes = dfs(grev,n)
    leaders = {}
    explored = [False]*n


    fTimes.reverse()
    for i in fTimes:
        if not explored[i]:
            lead = i
            count = 0
            count = _kosaraju(g, explored, lead)
            leaders[lead] =  count

    return leaders



g,  n, grev = read_graph("./SCC.txt")
print(len(g),n,g[0],g[1],g[2])

print("recursion limit",sys.getrecursionlimit())
sys.setrecursionlimit(n*2)
print("recursion limit",sys.getrecursionlimit())


# fTimes = dfs(g,n)
# print(fTimes[0:20],fTimes[-1:-20:-1])

s = time.time()

groups = kosaraju(g, n,grev)

sorted_dict = sorted(groups.items(), key=lambda item: item[1],reverse=True)

vals = []
for k,v in sorted_dict:
    vals.append(v)

e = time.time()

print("answer= ",vals[0:10])
print("run time=",e-s)


# g_test={
#     0:[1,3,5],
#     1:[2,],
#     2:[3,],
#     3:[1,],
#     4:[3,1,5],
#     5:[6,],
#     6:[0,]
# }
# groups = kosaraju(g_test, 7)

# sorted_dict = sorted(groups.items(), key=lambda item: item[1],reverse=True)
# print(sorted_dict[0:6])