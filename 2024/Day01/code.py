import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from AOCHelper import * 
input = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)

def parseInput():
    l, r = map(list,zip(*[map(int, line.split()) for line in input]))
    l.sort()
    r.sort() 

    return l,r    

def main():
   readinput("input.txt")
   first_star()       
   second_star()

def first_star():
    l, r = parseInput()
       
    print("Result First Star")
    print(sum(abs(l - r) for l,r in zip(l, r)))

def second_star():
    l, r = parseInput() 
 
    print("Result Second Star")
    print(sum(c * r.count(c) for c in l))

if __name__ == '__main__':
    main()