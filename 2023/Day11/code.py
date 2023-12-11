import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,galaxies,empty_rows,empty_cols
    input = readinput_lines(filename)
    empty_rows = [r for r, row in enumerate(input) if all(ch == "." for ch in row)]
    empty_cols = [c for c, col in enumerate(zip(*input)) if all(ch == "." for ch in col)]
    galaxies = [(r, c) for r, row in enumerate(input) for c, ch in enumerate(row)  if ch == "#"]
       
def main():
    readinput("input_ex.txt")
    first_star()
    second_star()

def first_star():
    print("Result First Star")
    print(calculate_distances(1))

def calculate_distances(offset):
    tot = 0
    for galaxy in itertools.combinations(galaxies,2):
        tot+= manhattan(galaxy[0],galaxy[1]) 
        for row in empty_rows:
            if isbetween(row, galaxy[0][0] , galaxy[1][0]):
                tot+= offset
        for col in empty_cols:
            if isbetween(col,galaxy[0][1] , galaxy[1][1]):
                tot+= offset
    return tot
def second_star():
    tot = 0
    # to low 265829033566
    # 560822911938
    
    print("Result Second Star")
    print(calculate_distances(1_000_000-1))
if __name__ == '__main__':
    main()