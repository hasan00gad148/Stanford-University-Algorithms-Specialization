from itertools import combinations
import math
import time

def read_graph(filename):

    f = open(filename, 'r')
    lines = f.readlines()
    n= int(lines[0])
    lines = lines[1:]

    cities= []
    for line in lines:
        cities.append(list(map(float, line.split())))

    return cities,n



def distances(cities,n):
    distances = [None]*n
    k = 0
    for i in cities:
        for j in cities:
            if distances[k] is not None:
                distances[k].append(math.sqrt((j[0]-i[0])**2+(j[1]-i[1])**2))
            else:
                distances[k] = [math.sqrt((j[0]-i[0])**2+(j[1]-i[1])**2),]
        k+=1

    return distances



def tsp(cities,distances,n):

    tprev = {}
   
    for i in range(1,n):
        s = str(set((i,)))
        tprev[(s,i)] = distances[i][0]

    for i in range(2,n):
        tcurr = {}
        for s in combinations(range(1,n), i):

            s_ = set(s)
            s_1=str(s_)
            for j in s:
               
                s_2 = str(s_-{j})
                tcurr[(s_1,j)] = float("inf")
                for k in s:
                    if k == j: continue
                    tcurr[(s_1,j)] = min(tprev.get((s_2,k),float("inf")) + distances[k][j],  tcurr[(s_1,j)])

        tprev.clear()
        tprev = tcurr
        

    s =str(set(range(1,n)))
    tcurr[(s,0)] = float("inf")
    for k in range(1,n):
        tcurr[(s,0)] = min(tcurr.get((s,k),float("inf")) + distances[0][k], tcurr[(s,0)] )


    return tcurr[(s,0)]




cities, n = read_graph("./test1.txt")
distances_ = distances(cities,n)
ans =  tsp(cities, distances_, n)
print(ans)

cities, n = read_graph("./test2.txt")
distances_ = distances(cities,n)
ans =  tsp(cities, distances_, n)
print(ans)


cities, n = read_graph("./test3.txt")
distances_ = distances(cities,n)
ans =  tsp(cities, distances_, n)
print(ans)

s = time.time()
cities, n = read_graph("./tsp.txt")
# n = 20
# cities = cities[:n]
distances_ = distances(cities,n)
ans =  tsp(cities, distances_, n)
e = time.time()
print("answer is: ",ans,"\t","it took time: ",e-s)