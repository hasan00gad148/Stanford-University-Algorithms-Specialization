import math

def karastuba(x,y):

    if x==0 or y == 0 or math.floor(math.log10(x)+1)==1 or math.floor(math.log10(y)+1)==1:
        return x*y
    else:
        n = max(math.floor(math.log10(x)+1), math.floor(math.log10(y)+1))

        
        a = x//(10**(n//2))
        b = x % (10**(n//2))
        c = y//(10**(n//2))
        d = y%(10**(n//2))
     
        
        
        ac = karastuba(a,c)
        bd = karastuba(b,d)
        ad_bc = karastuba(a+b, c+d) -ac -bd
        
        product = 10**(2*(n//2))*ac +10**((n//2))*(ad_bc) + bd
        return product

n1 = 5634
n2 = 95425


print("karastuba =",karastuba(n1,n2),end="\n")

print("python =",n1*n2,end="\n")

if n1*n2 == karastuba(n1,n2):
    print("algo is correct",end="\n")
else:
    print("algo is wrong",end="\n")