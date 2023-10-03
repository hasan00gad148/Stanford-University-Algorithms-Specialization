import os

project_dir = os.path.dirname (os.path.abspath (__file__))

def read_file(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    n = int(lines[0])
    lines = lines[1:]

    jobs = []
    for line in lines:
        l = line.split()
        l = list(map(int, l))
        jobs.append(l)
    
    return jobs,  n


def maxWeightedSum_difference(jobs, n):
    jobs.sort(key=lambda x: ((x[0]-x[1]),x[0]), reverse=True)

    finishTime = 0
    sum = 0
    for j in jobs:
        finishTime += j[1]
        sum += (j[0]*finishTime)
    
    return sum


def maxWeightedSum_ratio(jobs, n):
    jobs.sort(key=lambda x: ((x[0]/x[1]),x[0]), reverse=True)

    finishTime = 0
    sum = 0
    for j in jobs:
        finishTime += j[1]
        sum += (j[0]*finishTime)
    
    return sum



jobs, n = read_file(project_dir+'\\jobs.txt')

sum_difference = maxWeightedSum_difference(jobs, n)

print (sum_difference)



jobs, n = read_file(project_dir+'\\jobs.txt')

sum_ratio = maxWeightedSum_ratio(jobs, n)

print (sum_ratio)

