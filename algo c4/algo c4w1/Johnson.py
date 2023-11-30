from dijkstra import dijkstra
from bellman_ford import bellman_ford



def read_graph(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    n,m = list(map(int,lines[0].split()))
    lines = lines[1:]
    g = [None]*n
    for line in lines:
        u,v,w = list(map(int,line.split()))
        if g[u-1] is None:
            g[u-1]=[[v-1,w],]
        else:
            g[u-1].append([v-1,w])

    return g,n,m




def get_weights(g,n):

    g.append([[i,0] for i in range(n)])
    weights = bellman_ford(g,n,-1)
    g.pop()

    return weights 




def reweight_all_positive(g,n,weights):
    for i in range(n):
        for j in range(len(g[i])):
            v,w = g[i][j]
            g[i][j][1] += (weights[i]-weights[v])    





def n_dijkstras(g,n):
    table = []
    for i in range(n):
        # print(i+1)
        table.append(dijkstra(g,n,i))
        

    return table





def reweight_original(table,n,weights):
    for i in range(n):
        for j in range(len(table[i])):
            table[i][j] -= (weights[i]-weights[j])  


def get_shortest_shortest_path(table,n):
    min_length = float("inf")
    for i in range(n):
        for j in range(n):
            if i == j: continue
            min_length = min(min_length, table[i][j])

    return min_length






g,n,m = read_graph("./g3.txt")
weights = get_weights(g,n)
if weights :
    reweight_all_positive(g,n,weights)
    table = n_dijkstras(g,n)
    reweight_original(table,n,weights)
    ans = get_shortest_shortest_path(table,n)
    print (ans)
else:
    print("Graph contains negative  cycle")
