
class MaxHeap:
 
    def __init__(self,ARR=[],flag=True):

        if flag:
            self.heap =  list(range(len(ARR)))
            self.size = len(self.heap)
        else:
            self.heap =  []
            self.size = 0


    def heapify(self):
        l = list(range(self.size))
        l.reverse()
        for i in l:
            self.pubbleDownRec(i)
    
    

    def swap(self,i,j):
        tmp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = tmp


    def pubbleUpRec (self,i=0):
        j = (i-1)//2
        if j < 0:
            return
        if self.heap[i] > self.heap[j]:
            self.swap(i,j)
            self.pubbleUpRec(j)
        

    def pubbleDownRec (self,i=0):
        j1 = i*2+1
        j2 = i*2+2
        
        if (j1 < self.size)  and (self.heap[i] < self.heap[j1]):
            if (j2 < self.size)  and(self.heap[j1] < self.heap[j2]):
                self.swap(i,j2)
                self.pubbleDownRec(j2)
            else:
                self.swap(i,j1)
                self.pubbleDownRec(j1)               
        elif (j2 < self.size)  and(self.heap[i] < self.heap[j2]):
            self.swap(i,j2)
            self.pubbleDownRec(j2)
        else:return


    def extractMax (self):
        if self.size==0 :
            return None
        
        self.swap(0,-1)

        min = self.heap.pop()
        self.size = len(self.heap)
        # min = self.arr[min]
        self.pubbleDownRec(0)
        
        return min
    
    def peekMax(self):
        if self.size==0 :
            return None
        return self.heap[0]



    def add (self,i):
        self.heap.append(i)
        # self.swap(0,-1)
        self.size = len(self.heap)
        self.pubbleUpRec(self.size-1)


    def arrayOfIndeces(self):
        ar =[]
        while self.heap:
            ar.append(self.extractMax())
        return ar

       



# test_list = [45, 32, 18, 27, 39, 11, 24, 36, 9, 15, 42, 30, 6, 12, 33, 21, 3, 48, 54, 51]
# test_list2 = [76, 63, 49, 58, 70, 22, 43, 65, 18, 27, 75, 54, 15, 21, 59, 42, 9, 86, 97, 92, 81, 68, 34, 51, 78, 57,
#               12, 24, 66, 48, 6, 33, 60, 36, 3, 69, 72, 84, 90, 99, 45, 61, 30, 39, 64, 50, -1, -5 -8 -10]


# heap = MaxHeap(test_list2,False)
# for i,v in enumerate(test_list2):
#     heap.add(v)


# arr = heap.arrayOfIndeces()

# print (arr)


    







