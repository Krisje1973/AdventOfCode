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
   first_star()
   second_star()

def first_star():
    result = 0
    th = TupleHelper()
    regions = []
    seen = set()
    
    # loop 
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            t = (x,y)
            loop = deque([t])
            if t in seen : continue
            seen.add(t) 
            region = {t}
            while len(loop):
                r,c = loop.popleft()
                p = input[r][c]
                for nc,nr in th.get_neighbours((c,r),1,(len(input),len(row)),NeighbourghType.EXCLUDEDIAGONALS,True):
                    if (nr, nc) in region: continue
                    if p != input[nr][nc] : continue

                    region.add((nr, nc))
                    loop.append((nr, nc))

            seen = seen.union(region)
            result += len(region) * sum(4 - sum((nr, nc) in region for nr, nc in th.get_neighbours_array((x,y))) for y, x in region)

    print("Result First Star")
    print(result)


def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()