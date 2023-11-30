from minHeap import MinHeap

def dijkstra(g,n, s=0):

    weights = [float("inf")]*n
    heap = MinHeap(weights,flag=False)

    weights[s] = 0
    heap.add(s)


    while heap.size:
        u = heap.extractMin()

        for v,w in g[u]:
            
            if weights[v] > (weights[u]+w):
                weights[v] = (weights[u]+w)
                heap.add(v)

    return weights





# graph = [
#      [(1, 2), (3, 1)],
#      [(2, 3), (4, -5)],
#     [(5, 1)],
#      [(4, 2)],
#      [(5, 3)],
#      []
# ]
# w = dijkstra(graph, 6, 0)
# print(w)