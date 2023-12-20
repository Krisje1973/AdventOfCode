import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
digplan = defaultdict(str)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,digplan
    CH = Compass()
    input = readinput_lines(filename)
    for line in input:
        d,l,c = line.split()
        match d:
            case "U":
                d = (-1,0)
            case "D":
                d  = (1,0)
            case "R":
                d = (0,1)
            case "L":
                d = (0,-1)

        digplan[c] = (d,int(l))
    
def main():
   readinput("input_ex.txt")
   first_star()
   second_star()

def first_star():
    TH = TupleHelper()
    grid = set()
    pos = (0,1)
    mar,mac,mir,mic = 0,0,0,0
    for dig in digplan:
        d = digplan[dig][0]
        l= digplan[dig][1]

        for i in range(l):
            pos = TH.add_tuples(pos,d)
            grid.add(pos)
    
    rows = [d[0] for d in grid]
    cols = [d[1] for d in grid]
    minr = min(rows)
    maxr = max(rows)
    minc = min(cols)
    maxc = max(cols)

    print(minr,maxr,minc,maxc)
    grid = sorted(grid)
    last = None
    mic,mac,tot = 0,0,0
      
    gg = []
    for i in range(minr,maxr+1):
        gg.append(["."])
        for _ in range(minc,maxc+1):
            gg[i].append(".")   

    for r,c in grid:
       gg[r][c] = "#"

    print("Result First Star")
    grid = []
    for row in gg:
        s = "".join(row)
        grid.append(s)
    
    print(grid)
    cc="."
    for row in grid:
        cc.pop()
        print(row.split(".#"))

        

def second_star():
   
    print("Result Second Star")
 
if __name__ == '__main__':
    main()