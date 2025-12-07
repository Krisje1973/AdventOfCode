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
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    #1881 = to high
    gh = GridHelper()
    start = get_start()
    beams = set()
    beams.add(start)
    seen = set()
    splitters = set()
    maxx = len(input[0]) -1
    maxy = len(input) -1

    result = 0
    while beams:
        x,y = beams.pop()
        if (x,y) in seen:
            continue

        nexty = min(y+1,maxy)
       
        if input[y][x] == "^":
            result += 1
            print(f"Hit target at {(x,y)} total {result}")
            beams.add((x-1,nexty))
            beams.add((x+1,nexty))
        else:
            if y == maxy:
                continue
            beams.add((min(x,maxx),nexty))
        
        seen.add((x,y))
    print("Result First Star")
    print(result)
    print([x for x,y in splitters if y==14])

def second_star():
    print("Result Second Star")
def get_start():
    start = (0,0)
    for row,line in enumerate(input):
        for col,val in enumerate(line):
            if val == "S":
                return (col,row)
if __name__ == '__main__':
    main()