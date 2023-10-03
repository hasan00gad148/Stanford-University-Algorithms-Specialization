

class UnionFind:
    
    def __init__(self,n):
        self.parents = list(range(n))

    
    def find(self,i):
        if self.parents[i] == i:
            return self.parents[i]
        else: 
            return self.find(self.parents[i])
        
    def union(self,i,j):
        i_ = self.find(i)
        j_ = self.find(j)
        self.parents[i_] = j_
       



# test_list = [45, 32, 18, 27, 39, 11, 24, 36, 9, 15, 42, 30, 6, 12, 33, 21, 3, 48, 54, 51]
# test_list2 = [76, 63, 49, 58, 70, 22, 43, 65, 18, 27, 75, 54, 15, 21, 59, 42, 9, 86, 97, 92, 81, 68, 34, 51, 78, 57,
#               12, 24, 66, 48, 6, 33, 60, 36, 3, 69, 72, 84, 90, 99, 45, 61, 30, 39, 64, 50, -1, -5 -8 -10]


# heap = MinHeap(test_list2,False)
# for i,v in enumerate(test_list2):
#     heap.add(i)


# arr = heap.arrayOfIndeces()

# print(arr)


    







