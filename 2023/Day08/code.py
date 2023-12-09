import math
import functools ,itertools
import os, sys
import collections
from math import gcd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
dirs = defaultdict(str)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    for line in input[2:]:
        a,b = line.split("=")
        b=b.replace('(','').replace(')','').split(",")
        dirs[a.strip()] = (b[0].strip(),b[1].strip())
    
def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    instructs = collections.deque([s for s in (input[0])])
    ct = 0
    s = "AAA"
    while s != "ZZZ":
        ct+=1
        s = dirs[s]["LR".index(instructs[0])]
        instructs.rotate(-1)
    
    print("Result First Star")
    print(ct)
 
def second_star():
    cr  = ChineseReminder()
    instructs = collections.deque([s for s in (input[0])])
    counts = []
    for s in  [x for x in dirs if x[2] == "A"]:
        ct = 0
        while s[2] != "Z":
            ct+=1
            s = dirs[s]["LR".index(instructs[0])]
            instructs.rotate(-1)
        counts.append(ct)
    
    tot = 1
    for num in counts:
        tot = tot * num // gcd(tot, num)
    print("Result Second Star")
    print(tot)
    print("Result Second Star Chinese Remainder")
    print(cr.calculate_chinese_remainder([0 for x in counts],counts)[1])

if __name__ == '__main__':
    main()