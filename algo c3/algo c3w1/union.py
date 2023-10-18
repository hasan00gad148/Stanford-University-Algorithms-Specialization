

class UnionFind:
    
    def __init__(self,n):
        self.parents = list(range(n))
        self.rank = [0]*n
    
    def __find(self,i):
        if self.parents[i] == i:
            return self.parents[i]
        else: 
            return self.find(self.parents[i])
    
    def find(self,i):
        i_ = self.__find(i)
        self.parents[i] = i_
        return i_
        
    def union(self,i,j):
        i_ = self.find(i)
        j_ = self.find(j)
        if self.rank[i_] > self.rank[j_]:
            self.parents[j_] = i_
        elif self.rank[i_] < self.rank[j_]:
            self.parents[i_] = j_
        else:
            self.parents[i_] = j_
            self.rank[i_] += 1
            
       
       

    







