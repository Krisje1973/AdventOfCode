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
    input = readinput_lines(filename)
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    tot = 0
    transposed = list(map("".join,zip(*input)))
    back = []
    for line in transposed:
        n=""
        for c in line.split("#"):
            n+="#"
            n += "".join(sorted(c,reverse=True))
        back.append(n)
    back = list(map("".join,zip(*back)))[1:]
    for i,c in enumerate(back):
        tot+= c.count("O") * (len(input) - i)
        
    print("Result First Star")
    print(tot)


def second_star():
    global input
    #106390
    cache = defaultdict(list)
    for i in range(1,1001):
        key = "\n".join(input)
        if key in cache:
            input = cache[key]
        else:        
            input = tilt(input)  
            cache[key] = input
           
    tot = 0
    for i,c in enumerate( input):
        tot+= c.count("O") * (len(input) - i)
    print("Result Second Star")
    print(tot)

def tilt(grid):
    transposed = list(map("".join,zip(*grid)))
    back = []
    for line in transposed:
        n=""
        for c in line.split("#"):
            n+="#"
            n += "".join(sorted(c,reverse=True))
        back.append(n)
    
    grid=list(map("".join,zip(*back)))[1:]
    back = []
    for line in grid:
        n="#"
        for c in line.split("#"):
            if n != "":
                n+="#"
            n += "".join(sorted(c,reverse=True))
        back.append(n[2::])
    grid = back
    grid = list(map("".join,zip(*grid)))
    back = []
    for line in grid:
        line = line[::-1]
        n="#"
    
        for c in line.split("#"):
            n+="#"
            n += "".join(sorted(c,reverse=True))
        back.append(n[2::])
    grid=list(map("".join,zip(*back)))
    grid = grid[::-1]
    back = []
    for line in grid:
        n="#"
        for c in line.split("#"):
            if n != "":
                n+="#"
            n += "".join(sorted(c,reverse=False))
        back.append(n[2::])
    grid = back
    
    return grid
if __name__ == '__main__':
    main()