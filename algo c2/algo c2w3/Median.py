from minHeap import MinHeap
from maxHeap import MaxHeap



def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    arr = list(map(int, lines))
    return arr

class Median():
    def __init__(self):
        self.minLarge = MinHeap([],flag=False)
        self.maxSmall= MaxHeap([],flag=False)



    def balance(self):

        bf = self.minLarge.size - self.maxSmall.size

        while bf > 1:
            v = self.minLarge.extractMin()
            self.maxSmall.add(v)
            bf = self.minLarge.size - self.maxSmall.size


        while bf < -1:
          
            v = self.maxSmall.extractMax()
            self.minLarge.add(v)
            bf = self.minLarge.size - self.maxSmall.size




    def add(self,v):

        mnlarge = self.minLarge.peekMin()
        mxsmall = self.maxSmall.peekMax()

        if mnlarge and mnlarge <= v:
            self.minLarge.add(v)
        elif mxsmall and mxsmall >= v:
            self.maxSmall.add(v)
        else:
            self.maxSmall.add(v)
        
        self.balance()


    def addList(self,l):
        for i in l:
            self.add(i)

    def getMedian(self):
        nlarge = self.minLarge.size
        nsmall = self.maxSmall.size

        if nlarge == nsmall:
            return self.maxSmall.peekMax()
   
        elif nsmall < nlarge:
            return self.minLarge.peekMin()
        
        elif nsmall > nlarge:
            return self.maxSmall.peekMax()
        
        else: return None

        

    



arr = read_file('Median.txt')

median = Median()

m = 0
for v in arr:
    median.add(v)
    m += median.getMedian()

print (m%10000)
    
        