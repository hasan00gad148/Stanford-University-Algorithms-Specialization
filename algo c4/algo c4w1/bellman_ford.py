

def bellman_ford(g,n,s):
    table = [float("inf")] * n
    table[s] = 0

    lasti = 0
    for i in range(1,n+1):
        for u in range(n):
            for v,w in g[u]:
                if table[v] > (table[u] + w):
                    table[v] = table[u] + w
                    lasti = i

    if lasti == n:
        print("Graph contains negative  cycle (bellman ford function)")
        return None
    else:
        return table