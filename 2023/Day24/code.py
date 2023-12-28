import math
import functools ,itertools
import os, sys
import sympy
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
hailstones = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,hailstones
    input = readinput_lines(filename)
    hailstones = [tuple(map(int,line.replace("@",",").split(","))) for line in input]
def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    
    mil,mal = 200000000000000,400000000000000
    tot = 0
    for idx,h1 in enumerate(hailstones):
        for h2 in hailstones[:idx]:
            px,py = sympy.symbols("px py") 
            ans = sympy.solve([vy * (px - sx) - vx * (py - sy) for sx, sy, _, vx, vy, _ in [h1,h2]])
            
            if ans == [] : continue

            x,y = ans[px], ans[py]
            if mil <= x <= mal and mil <= y <= mal:
                if all((x-sx) * vx >=0 and (y-sy) * vy >= 0 for sx,sy,_,vx,vy,_ in [h1,h2]):
                    tot += 1
    print("Result First Star")
    print(tot)
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()