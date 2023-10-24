class Node():
    def __init__(self, name, value, isleaf, depth,left,right):
        self.name = name
        self.value = value
        self.isleaf = isleaf
        self.depth = depth
        self.left = left
        self.right = right

from minHeap import MinHeap

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n  = int(lines[0])
    lines = lines[1:]
    nodesHeap = MinHeap()

    for i,v in enumerate(lines):
        node = Node(str(i),int(v),True,0,None,None)
        nodesHeap.add(node)

    return nodesHeap,n

def huff(nodes:MinHeap,n):
   

    while nodes.size>1:
        a = nodes.extractMin()
        b = nodes.extractMin()
        ab = Node(a.name+"_"+b.name,a.value+b.value,False,0,a,b)
        nodes.add(ab)
    
    return nodes.extractMin()

leaves =[]     
def getDepth(root:Node,n):
    global leaves
    if root is  None :
        return 
    if root.isleaf :
        leaves.append(root.depth)
        return
    root.left.depth = root.depth + 1
    root.right.depth = root.depth + 1
    getDepth(root.left,n)
    getDepth(root.right,n)
    return root

     




nodes,n = read_file("./huffman.txt")
root = huff(nodes,n)
root = getDepth(root,n)
print(min(leaves), max(leaves))
