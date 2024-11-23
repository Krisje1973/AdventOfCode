import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = [list(map(int,line.replace("~",",").split(","))) for line in readinput_lines_no_strip_no_enter(filename)]
    
def main():
   readinput("input.txt")
   first_star()
   second_star()

def overlaps(a,b):
    # intersects when max van starts lower then min ends
    return max(a[0],b[0]) <= min(a[3],b[3]) and max(a[1],b[1]) <= min(a[4],b[4]) 

def first_star():
    input.sort(key=lambda brick : brick[2]) # z = height !
    for i,brick in enumerate(input):
        max_z = 1 # lowest
        for check in input[:i]: # run all lower bricks to check on, the max_z is the highest end of lower + 1 
            if overlaps(brick,check):
                max_z = max(max_z,check[5]+1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z
    input.sort(key= lambda brick:brick[2])

    k_supports_v = {i:set() for i in range(len(input))}
    v_supports_k = {i:set() for i in range(len(input))}
    
    for j,upper in enumerate(input):
        for i,lower in enumerate(input[:j]):
            if overlaps(upper,lower) and upper[2] == lower[5] + 1: 
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    total = 0

    for i in range(len(input)):
        if all(len(v_supports_k[j])>=2 for j in k_supports_v[i]):
            total+=1

    print("Result First Star")
    print(total)
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()