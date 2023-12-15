import math
import functools ,itertools
import os, sys
import numpy as np
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
patterns = defaultdict(list)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,patterns
    input = readinput_lines(filename)
    pattern = []
    i=0
    for line in input:
        if line=="":
            i+=1
        else: patterns[i].append(line)

def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    tot = 0
    for pattern in patterns.values():
        tot+= find_mirror(pattern) * 100 + find_mirror(list(zip(*pattern)))

    print("Result First Star")
    print(tot)

# def find_mirror(pattern):
#     for r in range(1, len(pattern)):
#         if pattern[r:][:len(pattern[:r][::-1])] == pattern[:r][::-1][:len(pattern[r:])]:
#             return r
        
#     return 0
        
def get_hlines(grid: list[list[str]]) -> list[int]:
    n = len(grid)
    ans = []
    for i in range(n-1):
        r1 = reversed(range(0, i+1))
        r2 = range(i+1, n)
        if all(grid[x] == grid[y] for x, y in zip(r1, r2)):
            ans.append(i)
    return ans

def getlines(grid: list[list[str]]):
    h_lines = get_hlines(grid)
    v_lines = get_hlines(list(zip(*grid[::-1])))
    return [
        *map(lambda x: ("H", x, 100*(x+1)), h_lines),
        *map(lambda x: ("V", x, x+1), v_lines),
    ]
def second_star():
    tot = 0

    print("Result Second Star")
    print(tot)
if __name__ == '__main__':
    main()