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
    maxx = len(input[0])
    maxy = len(input)

    result = 0
    while beams:
        x,y = beams.pop()
        seen.add((x,y))
        if input[y][x] == "^":
            result += 1
            splitters.add((x,y))
            for npos in gh.get_adjacent_pos_with_diag(x,y,maxx,maxy):
                xx,yy = npos
                if yy <= y or xx == x:
                    continue
                if npos not in seen:
                    beams.add(npos)
        else:
            if y == 14:
                pass
            if y == maxy -1:
                continue
            beams.add((min(x,maxx),min(y+1,maxy)))
    
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