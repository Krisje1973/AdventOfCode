import math
import functools ,itertools
import os, sys
import numpy as np
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
   first_star()
   second_star()

def first_star():
    # Shoelace formula
    # picks theorym
 
    xs = [0]
    ys = [0]
    x = y = 0
    b = 0
    for line in input:
        d,n,_ = line.split()
        n = int(n)
        b+=n
        if d == "R":
            x += n
        if d == "L":
            x -= n
        if d == "U":
            y -= n            
        if d == "D":
            y += n
        
        xs.append(x)
        ys.append(y)

    print("Result First Star")
    print(shoelace(xs,ys,b))

def second_star():
    xs = [0]
    ys = [0]
    x = y = 0
    b = 0
    for line in input:
        _,_,code = line.split()
        code = code.replace("#","").replace("(","").replace(")","")
        
        d = "RDLU"[int(code[-1])]
        n = int(code[:5],16)
        b+=n
        if d == "R":
            x += n
        if d == "L":
            x -= n
        if d == "U":
            y -= n            
        if d == "D":
            y += n
        
        xs.append(x)
        ys.append(y)

    print("Result Second Star")
    print(shoelace(xs,ys,b))

if __name__ == '__main__':
    main()