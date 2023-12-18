import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
groups = {}
seen = {}
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input, conditions
    ip = readinput_lines(filename)
    for idx,line in enumerate(ip):
        sp = line.split()
        input.append(sp[0])
        groups[idx] = list(map(int,sp[1].split(",")))

def main():
   readinput("input_ex.txt")
   #first_star()
   second_star()

def first_star():
    tot = 0
    tots=[]
    for idx,line in enumerate(input):
        to=0
        print(idx)
        replacements = getReplacements(line,"#.","?")
        for s in replacements:
            if s in seen:
                val = seen[s]
            else : val = validate(s)
            seen[s] = val
            if val == groups[idx]:
                tot+=1
                to +=1
        if to==1:
            tots.append(idx)

    print("Result First Star")
    print(tot,len(tots))

def second_star():
    tot = 0
    for idx,line in enumerate(input):
        s = line
        groups[idx] = groups[idx] * 5
        for _ in range(4):
            s += "?" + line
        print(s)
        #replacements = getReplacements(s,"#.","?")
        #print(replacements[0].replace("#","1").replace(".","0"),groups[idx],len(replacements))
    
        #tot+= validate_recursive(s,groups[idx])
   
    print("Result Second Star")
    print(tot)

def validate_recursive(springs,groups):
   
    if springs=="":
        return 1 if not len(groups) else 0
    if len(groups) == 0:
        return 0 if "#" in springs else 1

    s,g,l = springs[0],groups[0],len(springs)
    tot=0
    
    tot = 0
    # 
    if s in ".?":
        return validate_recursive(springs[1:],groups)
    if s in "#?":
        if g <= l and not "." in springs[1:] and (g == l or springs[g] != "#"):
            tot+= validate_recursive(springs[g + 1:], groups[1:])

        
    print(springs,tot)
    return tot

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

def validate2(s):
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

if __name__ == '__main__':
    main()