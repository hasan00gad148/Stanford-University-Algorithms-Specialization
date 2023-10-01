import sys

f = open("inversions.txt", "r")
l = list(map(int, f.readlines()))
print(len(l))
print(type( l[0]))

l2=[7,6,5,4,3,2,1]
l3=[9,8,7,6,5,4,3,2,1]
def inversion(l:list,lt,start,end):
    count=0
    if start < end:

        mid = int((start+end)/2)

        count += inversion(l,lt,start,mid)
        count += inversion(l,lt,mid+1,end)

        j = start 
        k = mid+1
        i = start

        while j <= mid and k <= end:
            if l[j] <= l[k]:
                lt[i] = l[j]
                j+= 1 
                i+= 1
            else:
                lt[i] = l[k]
                k+= 1 
                i+= 1
                count +=(mid-j+1)


        while j < mid+1:
            lt[i] = l[j]
            i+= 1
            j += 1

        while k < end+1:
            lt[i] = l[k]
            i+= 1           
            k += 1

        # Copy the sorted subarray into Original array
        for loop_var in range(start, end+1):
            l[loop_var] = lt[loop_var]




    return count

lt=[0]*7
print(str(inversion(l2,lt,0,6)))