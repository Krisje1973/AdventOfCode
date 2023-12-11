import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
galaxies =[]
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,galaxies,empty_rows,empty_cols
    input = readinput_lines(filename)
    empty_rows = []
    empty_cols = []
    galaxies = []
    for ri, row in enumerate(input):
        h = [input[ri][x]=="." for x in range(len(input[0]))]  
        if all(c for c in h):
            empty_rows.append(ri)
    for ci, col in enumerate(input[0]):
        v = [input[x][ci]=="." for x in range(len(input))]  
        if all(c for c in v):
           empty_cols.append(ci)

    newInput = []
    for r,row in enumerate(input):
        newInput.append("")
        for c,col in enumerate(row):
            if c in empty_cols:
                newInput[-1] += "."
            newInput[-1] += col
        if r in empty_rows:
            newInput.append(newInput[-1])

    #input = newInput

    for r, row in enumerate(input): 
        for c, ch in enumerate(row):
            if ch == "#":
                galaxies.append((r,c))
   
       
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
   
    tot = 0
    for galaxy in itertools.combinations(galaxies,2):
        tot+= manhattan(galaxy[0],galaxy[1]) 
        
    print("Result First Star")
    print(tot)

def isbetween(v: int, a: int, b: int) -> bool:
    if a > b: a, b = b, a
    return a < v < b   

def second_star():
    tot = 0
    # to low 265829033566
    # 560822911938
    
    for galaxy in itertools.combinations(galaxies,2):
        tot+= manhattan(galaxy[0],galaxy[1]) 
        for row in empty_rows:
            if isbetween(row, galaxy[0][0] , galaxy[1][0]):
                tot+= 1_000_000 - 1
        for col in empty_cols:
            if isbetween(col,galaxy[0][1] , galaxy[1][1]):
                tot+= 1_000_000 - 1
    
    print("Result Second Star")
    print(tot)
if __name__ == '__main__':
    main()