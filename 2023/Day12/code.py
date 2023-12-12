import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
conditions = {}
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input, conditions
    ip = readinput_lines(filename)
    for idx,line in enumerate(ip):
        sp = line.split()
        input.append(sp[0])
        conditions[idx] = list(map(int,sp[1].split(",")))

def main():
   readinput("input_ex.txt")
   first_star()
   second_star()

def first_star():
    tot = 0
    for idx,line in enumerate(input):
        print(idx)
        s = getReplacements(line,"#.","?")
        for s in getReplacements(line,"#.","?"):
            if validate(s) == conditions[idx]:
                tot+=1

    print("Result First Star")
    print(tot)
def validate(s):
    ct=0
    springs=[]
    for c in s:
        if c == "#":
            ct+=1
        else:
            if ct>0:
                springs.append(ct)
            ct=0

    if ct > 0: springs.append(ct)
    return springs

def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()