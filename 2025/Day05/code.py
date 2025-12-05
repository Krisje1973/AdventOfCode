import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\Devops\AdventOfCode")
from  AOCHelper import * 
input = []
#https://www.youtube.com/watch?v=IaPaQ5heqZs
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,ranges,ingr
    rang, ingr = readinput_as_pairs(filename)
    ingr = [int(i) for i in ingr]
    rang = [r.split("-") for r in rang]
    ranges = reduce_overlap_ranges(rang)
    
def main(): 
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    result = 0
    for i in ingr:
        for s,e in ranges:
            result += s <= i <= e
                 
    print("Result First Star")
    print(result)
 
def second_star():
    result = 0
    for s,e in ranges:
        result += e+1-s
        
    print("Result Second Star")
    print(result)
 
if __name__ == '__main__':
    main()

    