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
   #first_star()
   second_star()

def first_star():
    #1881 = to high
    start = get_start()
    beams = set()
    beams.add(start)
    seen = set()
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
            beams.add((x-1,nexty))
            beams.add((x+1,nexty))
        else:
            if y == maxy:
                continue
            beams.add((min(x,maxx),nexty))
        
        seen.add((x,y))

    print("Result First Star")
    print(result)

@cache
def drop_beam(x,y):
    maxx = len(input[0]) -1
    maxy = len(input) -1
    if y == maxy:
        return 1
    nexty = min(y+1,maxy)
    if input[y][x] == "^":
        return drop_beam(x-1,nexty) + drop_beam(x+1,nexty)
    else:
        return drop_beam(min(x,maxx),nexty)
    
def second_star():
    start = get_start()
    beams = []
    beams.append((0,start[0],start[1]))
    seen = set()
    maxx = len(input[0]) -1
    maxy = len(input) -1

    result = 0
    time = 0
    

    print("Result First Star")
    print(drop_beam(start[0],start[1]))

def get_start():
    for row,line in enumerate(input):
        for col,val in enumerate(line):
            if val == "S":
                return (col,row)
if __name__ == '__main__':
    main()