import sys
print("recursion limit",sys.getrecursionlimit())
sys.setrecursionlimit(2**20)
print("recursion limit",sys.getrecursionlimit())



def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n  = int(lines[0])
    lines = lines[1:]
    nodes = {}

    for i,v in enumerate(lines):
        nodes[i] = int(v)

    return nodes,n


def mwis_memo(nodes,mwis,n=0):
    if mwis.get(n,None) is not None:
        return mwis[n]
    if n >= len(nodes):
        return 0
    elif n == len(nodes)-1:
        mwis[n] = nodes[n]
        return  nodes[n]



    w1 = mwis_memo(nodes,mwis,n+1) 
    w0 = mwis_memo(nodes,mwis,n+2)+nodes[n]
    

    mwis[n] = max(w0, w1)
    return  mwis[n]
    


nodes, n = read_file("./mwis.txt")
mwis = {}
W = mwis_memo(nodes,mwis,0)
print(W)
l = [1, 2, 3, 4, 17, 117, 517, 997]
lmwis = []
keys = list( mwis.keys())
keys.reverse()

if mwis[keys[0]] < mwis[keys[1]]:
    keys = keys[1:]

i = 0
while i < len(keys):

    if (mwis.get(i+2,None)!=None and  mwis[i]-nodes[i] == mwis[i+2]) :
        lmwis.append(i)
        i+=1
    i+=1




    


s=[]
for i in l:
    if i-1 in lmwis: 
        s.append('1')
    else:
        s.append('0')

print("".join(s))


