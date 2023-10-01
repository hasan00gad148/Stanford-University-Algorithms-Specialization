from minHeap import MinHeap

def read_graph(filename):
    file = open(filename,"r")
    lines = file.readlines()

    g=[]
    n=0
    for line in lines:
        line = line.split('\t')
        n = max(n,int(line[0])-1)
        line = line[1:-1]

        neighbors = []
        for pair in line:
            pair = list(map(int,pair.split(',')))

            pair[0] = pair[0]-1
            n = max(n,pair[0])

            neighbors.append(pair)
            
        
        g.append(neighbors)

    return g, n+1




def dijkstra(g,n, s=0):

    weights = [None]*n
    heap = MinHeap(weights,flag=False)

    weights[s] = 0
    heap.add(s)


    while heap.size:
        u = heap.extractMin()

        for i in g[u]:
            v,w = i
            if weights[v] == None or weights[v] > (weights[u]+w):
                weights[v] = (weights[u]+w)
                heap.add(v)

    return weights







vertcies = [7,37,59,82,99,115,133,165,188,197]


g, n = read_graph('./dijkstra.txt')
w = dijkstra(g, n, 0)

# print(g[:2], n)

output = []
for i in vertcies:
    output.append(w[i-1])

print(output)