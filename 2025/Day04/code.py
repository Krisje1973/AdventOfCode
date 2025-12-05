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
   #first_star()
   second_star()

def first_star():
    gh = GridHelper()
    maxx = len(input[0])
    maxy = len(input)
    result = 0
    for row in range(maxy):
        for col in range(maxx):
            if input[row][col] != "@":
                continue
            sur = gh.get_adjacent_pos_with_diag(row,col,maxx,maxy)
            if sum([int(input[r][c] == "@") for r,c in sur]) < 4:
                result += 1
    print("Result First Star")
    print(result)
 
def second_star():
    global input
    gh = GridHelper()
    maxx = len(input[0])
    maxy = len(input)
    result = 0
    moved = True
    seen = set()
    while moved:
        moved = False
        for row in range(maxy):
            for col in range(maxx):
                if input[row][col] != "@" or (row,col) in seen:
                    continue
                sur = gh.get_adjacent_pos_with_diag(row,col,maxx,maxy)
                if sum([int(input[r][c] == "@" and (r,c) not in seen) for r,c in sur]) < 4:
                    result += 1
                    seen.add((row,col))
                    moved = True
    
    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()