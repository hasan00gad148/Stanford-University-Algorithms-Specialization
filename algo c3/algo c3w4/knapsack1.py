
def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    C,n  = list(map(int,lines[0].split()))
    lines = lines[1:]
    nodes = []

    for i in lines:
        nodes.append(list(map(int,i.split())))

    return nodes,C,n



def knapsack(nodes,C,n):
    table = [[0 for i in range(n+1)] for j in range(C+1)]
    
    for i in range(1,C+1):
        for j in range(1,n+1):
            if nodes[j-1][1] > i:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = max(nodes[j-1][0] + table[i-nodes[j-1][1]][j-1], table[i][j-1])
    

    return table[-1][-1]




nodes,C,n = read_file("./knapsack1.txt")

v = knapsack(nodes,C,n)

print(v)






