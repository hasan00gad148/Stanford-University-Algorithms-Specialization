

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    arr=[]
    for line in lines:
        arr.append(int(line))

        
    return arr


def _2sum(arr,targets=[]):


    dictArr = {} 
    for i in arr:
        if dictArr.get(i,None) != None:
            continue
        else:
            dictArr[i] = 1

    count = 0
    for t in targets:
        for k in dictArr.keys():
            if k == (t-k): continue
            if dictArr.get((t-k), None):
                count += 1
                
    return count





"""test  answer=8"""
# arr = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
# targets = [3,10]
# count = _2sum(arr,targets)
# print (count)

arr = read_file("2sum.txt")
targets = list(range(-10000,10001))

count = _2sum(arr,targets)
print (count)
