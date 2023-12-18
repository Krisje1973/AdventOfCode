import math
import functools ,itertools
from heapq import heappush, heappop
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
    seen = set()
    grid = input
    pq = [(0, 0, 0, 0, 0, 0)]
    ans = 0
    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            ans = hl
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + int(grid[nr][nc]), nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + int(grid[nr][nc]), nr, nc, ndr, ndc, 1))

    
    print("Result First Star")
    print(ans)
 
def second_star():
    seen = set()
    grid = input
    pq = [(0, 0, 0, 0, 0, 0)]
    ans = 0
    while pq:
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            ans = hl
            break

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + int(grid[nr][nc]), nr, nc, dr, dc, n + 1))

        if n >= 4 or (dc == 0 and dr ==0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heappush(pq, (hl + int(grid[nr][nc]), nr, nc, ndr, ndc, 1))
        
    print("Result Second Star")
    print(ans)

if __name__ == '__main__':
    main()