"""
needs log(n) * 2*n**2 iterations to have a success probability of 1/n

"""


import random
def read_file(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    n = int(lines[0])
    lines = lines[1:]

    constraints = []
    for line in lines:
        constraints.append(list(map(int, line.split())))

    return constraints, n


def SAT_2(constraints,n):
    ans = [random.randint(0, 1) for __ in range(n+1)]
    ans = [True if x else False for x in ans]

    
    for __ in range(10000):
        flag = True 
        for x,y in constraints:
            X = not ans[abs(x)] if x<0 else ans[x]
            Y = not ans[abs(y)] if y<0 else ans[y]

            if not (X or Y):
                flag = False             
                if random.randint(0, 1):
                    ans[abs(x)] = not ans[abs(x)]
                else:
                    ans[abs(y)] = not ans[abs(y)]
                break
                
                # countx = 0
                # ans[abs(x)] = not ans[abs(x)]             
                # for x_,y_ in constraints:
                #     X = not ans[abs(x_)] if x<0 else ans[x_]
                #     Y = not ans[abs(y_)] if y<0 else ans[y_]
                #     if (X or Y):
                #         countx+=1
                # ans[abs(x)] = not ans[abs(x)]
 
 
                # county = 0
                # ans[abs(y)] = not ans[abs(y)]             
                # for x_,y_ in constraints:
                #     X = not ans[abs(x_)] if x<0 else ans[x_]
                #     Y = not ans[abs(y_)] if y<0 else ans[y_]
                #     if (X or Y):
                #         county+=1
                # ans[abs(y)] = not ans[abs(y)]

                # if county > countx:
                #     ans[abs(y)] = not ans[abs(y)]
                # else:
                #     ans[abs(x)] = not ans[abs(x)]
                # break


        if flag:
            return True


    for x,y in constraints:
        X = not ans[abs(x)] if x<0 else ans[x]
        Y = not ans[abs(y)] if x<0 else ans[y]

        if not (X or Y):
            return False
    return True 
        





filenames = ["./2sat1.txt", "./2sat2.txt","./2sat3.txt","./2sat4.txt","./2sat5.txt","./2sat6.txt"]

constraints, n = read_file(filenames[0])

ans = SAT_2(constraints,n)

print(ans)





