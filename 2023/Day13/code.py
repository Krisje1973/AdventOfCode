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
   readinput("input_ex.txt")
   #first_star()
   second_star()

def first_star():
    tot = 0
    for pattern in patterns.values():
        tot+= find_mirror(pattern) * 100 + find_mirror(list(zip(*pattern)))

    print("Result First Star")
    print(tot)

def second_star():
    tot = 0
    row = find_mirror2(input)
    tot += row * 100

    col = find_mirror2(list(zip(*input)))
    tot += col

    print("Result Second Star")
    print(tot)
if __name__ == '__main__':
    main()