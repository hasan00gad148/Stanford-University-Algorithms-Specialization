import sys
print("recursion limit",sys.getrecursionlimit())
sys.setrecursionlimit(2**20)
print("recursion limit",sys.getrecursionlimit())



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
    table  = {}
    return knapsack_(nodes,table,C,n-1)

def knapsack_(nodes,table,C,n):
    if table.get(f"{n}_{C}",None) is not None:
        return table[f"{n}_{C}"]
    if n < 0 or C < 0:
        return 0




    w1 = knapsack_(nodes,table,C-nodes[n][1],n-1) + nodes[n][0] if C-nodes[n][1] >= 0 else 0 
    w0 = knapsack_(nodes,table,C,n-1)
    

    table[f"{n}_{C}"] = max(w0, w1)
    return  table[f"{n}_{C}"]
    






nodes,C,n = read_file("./knapsack_big.txt")

v = knapsack(nodes,C,n)

print(v)
