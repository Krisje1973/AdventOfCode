import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    
def main():
   readinput("input_ex.txt")
   #first_star()
   second_star()

def first_star():
    tiles = [list(map(int, line.strip().split(','))) for line in input]
   
    result=0
    for x, y in tiles:
        for xx, yy in tiles:
            result=max(result, (abs(x-xx)+1)*(abs(y-yy)+1))
   
    print(result)

def second_star():
    tiles = [list(map(int, line.strip().split(','))) for line in input]
    xs = defaultdict(list)
    ys = defaultdict(list)
    for tile in tiles:
        x,y = tile
        xs[x].append(y)
        ys[y].append(x)

    result=0
    grid = []
    for x in xs:
        xs[x].sort()
    
    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()