import random 


f = open("quickSort.txt", "r")
l = list(map(int, f.readlines()))
print(len(l))
print(type( l[0]))

f = open("quickSort.txt", "r")
l1 = list(map(int, f.readlines()))
print(len(l1))
print(type( l1[0]))

l2=[7,6,5,4,3,2,1,0]
l3=[9,8,7,6,5,4,3,2,1,0]
l4=[13,12,11,10,9,8,7,6,5,4,3,2,1,0]
l5=[13,12,1,9,10,8,8,6,5,4,3,2,11,0]



        

def choosePivot(arr,s,e):
    # rand = random.randint(s,e)
    # return rand

    first = arr[s]
    last = arr[e]
    m = int((e-s)/2)  if (e-s+1)%2 == 0 else int((e-s+1)/2)
    mid = arr[m+s]
    a = [first,mid,last]

    pivot = 0
    for i in range(len(a)):
        if a[i] != min(a) and a[i] != max(a):
            pivot =  i
            break
    if pivot == 0:
        return s
    elif pivot == 1:
        return m+s
    else: return e


    


def swap(arr,l,r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp



def partition(arr, s, e):
    l = s 
    pivot = s-1
    for r in range(s, e+1):
        if arr[pivot] >= arr[r]:

            swap(arr, l, r)
            l+=1 


    swap(arr, pivot, l-1)

    return l-1    

    
        

def quickSort(arr,s,e,f=0):
    if s >= e: return 0
  
    
    # choose pivot
    
    if f == 1:
        swap(arr, s,e)
    elif f== 2:
        p = choosePivot(arr, s, e)
        swap(arr, s, p)

    # partition 
    comparisons = (e-s)
    pivot = partition(arr, s+1, e)

    # divide

    if pivot != 0: comparisons +=  quickSort(arr, s, pivot-1,f) # left
    if pivot != e: comparisons +=  quickSort(arr, pivot+1, e,f) # right

    return comparisons






c = quickSort(l4, 0, len(l4)-1,2)
print(l4,c)

c = quickSort(l5, 0, len(l5)-1,2)
print(l5,c)



l.sort()
print(l[:20])

c = quickSort(l1, 0, len(l1)-1,2)
print(l1[:20],c)

for i in range(len(l)):
    if l[i]!=l1[i]:
        print("not correct")
        break