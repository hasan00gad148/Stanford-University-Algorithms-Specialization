import math
import time




def read_graph(filename):

    f = open(filename, 'r')
    lines = f.readlines()
    n= int(lines[0])
    lines = lines[1:]

    cities= []
    for line in lines:
        cities.append(list(map(float, line.split()[1:])))

    return cities,n




def tsp_nn(cities:list,n:int):

    s = set((0,))
    v = 0
    cost = 0
    for __ in range(n-1):
        
        d1 = float("inf")
        u = None
        for i in range(n):
            d2 = math.sqrt((cities[i][0]-cities[v][0])**2+(cities[i][1]-cities[v][1])**2)
            if i not in s and d2<d1:           
                d1 = d2
                u = i
        
        v = u 
        s.add(v)
        cost+=d1

    cost+= math.sqrt((cities[0][0]-cities[v][0])**2+(cities[0][1]-cities[v][1])**2)

    return cost
        

cities, n = read_graph("./test.txt")
ans =  tsp_nn(cities, n)
print(ans)#TSP:15.2361

cities, n = read_graph("./nn.txt")
ans =  tsp_nn(cities, n)
print(ans)