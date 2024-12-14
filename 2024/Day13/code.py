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
    
    input = readinput_as_pairs(filename)
   
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    claws = {}
    result = 0
    pattern = r"(Button A|Button B|Prize):\s*X[+=]?(\d+),\s*Y[+=]?(\d+)"
    for line in input:
        for claw in line:
            key, x, y = re.match(pattern,claw).groups()
            claws[key] = (int(x), int(y))

        ax,ay = claws["Button A"]
        bx,by = claws["Button B"]
        px,py = claws["Prize"]

        buta = set()
        for i in range(100):
            for j in range(100):
                if px == (ax * i) + (bx * j): 
                    buta.add((i,j))
        butb = set()
        for i in range(100):
            for j in range(100):
                if py == (ay * i) + (by * j): 
                    butb.add((i,j))

        wins = buta.intersection(butb)
        result+= sum(a*3+b*1 for a,b in wins)
        
    print("Result First Star")
    print(result)

def second_star():
    #875318608908 to low
    claws = {}
    result = 0
    pattern = r"(Button A|Button B|Prize):\s*X[+=]?(\d+),\s*Y[+=]?(\d+)"
    for line in input:
        for claw in line:
            key, x, y = re.match(pattern,claw).groups()
            claws[key] = (int(x), int(y))

        ax,ay = claws["Button A"]
        bx,by = claws["Button B"]
        px,py = claws["Prize"]

        px += 10000000000000
        py += 10000000000000

        # Point of intersection
        

        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            result += int(ca * 3 + cb)
     
    
    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()