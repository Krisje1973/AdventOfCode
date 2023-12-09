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
    #1939607041 to High
    #1939607039
    tot = 0
    for line in input:
        start = [[int(i) for i in line.split()]]
        extra = start
        while(True):
            new = getExtraPolation(extra)
            start.append(new)
            extra = [new]
            if all(x==0 for x in new):
                break
        for ex in start:
            tot+= ex[-1]
    
    print("Result First Star")
    print(tot)
 
def second_star():
    tot = 0
    for line in input:
        tot+= extraPolate(getNumbersFromString(line))
        
    print("Result Second Star")
    print(tot)

def extraPolate(hist):
    if all(i==0 for i in hist):
        return 0

    return hist[0] - extraPolate([y-x for x,y in list(zip(hist,hist[1::]))])

def getExtraPolation(seq):
    seq2 = []
    for idx,i in enumerate(seq[0][:len(seq[0])-1]):
        seq2.append(seq[0][idx+1] - i)
    return seq2      
  
if __name__ == '__main__':
    main()