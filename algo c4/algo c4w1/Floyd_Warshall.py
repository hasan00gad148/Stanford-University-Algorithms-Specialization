



def read_graph(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    n,m = list(map(int,lines[0].split()))
    lines = lines[1:]
    g = [None]*n
    for line in lines:
        u,v,w = list(map(int,line.split()))
        if g[u-1] is None:
            g[u-1]=[(v-1,w),]
        else:
            g[u-1].append((v-1,w))

    return g,n,m




def init_folyd_warshall(g,n,m):
    table = {}
    for i in range(n):
        table[f"{i}{i}{0}"] = 0
    for i in range(n):
        for j in g[i]:
            table[f"{i}{j[0]}{0}"]=j[1]

    return table




def floyd_warshall(g,n,m):
    table = init_folyd_warshall(g,n,m)

    for k in range(1,n):
        for i in range(n):
            for j in range(n):
                w = min(table.get(f"{i}{j}{k-1}",float("inf")),\
                                           (table.get(f"{i}{k}{k-1}",float("inf"))+\
                                            table.get(f"{k}{j}{k-1}",float("inf"))))
                table[f"{i}{j}{k}"] = w

    return table




def check_negative_cyclic(table,n,m):
    for i in range(n):
        if table[f"{i}{i}{-1}"]!=0:
            return True
    
    return False



def get_shortest_shortest_path(table,n,m):
    min_length = float("inf")
    for i in range(n):
        for j in range(n):
            if i == j: continue
            min_length = min(min_length, table[f"{i}{j}{-1}"])

    return min_length


g,n,m = read_graph("./g1.txt")
print(n,m,g[0])
table = floyd_warshall(g,n,m)
print(check_negative_cyclic(table,n,m))  
print(get_shortest_shortest_path(table,n,m))