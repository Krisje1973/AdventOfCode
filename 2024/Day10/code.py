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
    input =  [[int(c) for c in line.strip()] for line in readinput_lines(filename)]  
   
def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    result = 0
    rows = len(input)
    cols = len(input[0])
    trailheads = [(r,c) for r in range(rows) for c in range(cols) if input[r][c] == 0]
    th = TupleHelper()
    seen = set()
    for r,c in trailheads:
        seen = {(r,c)}
        path = deque([(r,c)])
        while len(path) > 0:
            row,col = path.popleft()
            cur = input[row][col]
            for nc,nr in th.get_neighbours((col,row),1,(cols,rows),NeighbourghType.EXCLUDEDIAGONALS,True):
                nei = input[nr][nc]
                if nei != cur + 1:
                    continue
                if (nr,nc) in seen: 
                    continue

                seen.add((nr,nc))

                if nei == 9:
                    result+=1
                else:
                    path.append((nr,nc))
                

    print("Result First Star")
    print(result)
    
 
def second_star():
    result = 0
    rows = len(input)
    cols = len(input[0])
    trailheads = [(r,c) for r in range(rows) for c in range(cols) if input[r][c] == 0]
    th = TupleHelper()
    seen = set()
    for r,c in trailheads:
        seen = {(r,c)}
        path = deque([(r,c)])
        while len(path) > 0:
            row,col = path.popleft()
            cur = input[row][col]
            for nc,nr in th.get_neighbours((col,row),1,(cols,rows),NeighbourghType.EXCLUDEDIAGONALS,True):
                nei = input[nr][nc]
                if nei != cur + 1:
                    continue
                if (nr,nc) in seen: 
                    continue

                #seen.add((nr,nc))

                if nei == 9:
                    result+=1
                else:
                    path.append((nr,nc))
    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()