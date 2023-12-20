import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
workflows = defaultdict(str)
parts = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,parts,workflows
    input = readinput_lines(filename)
    idx=0
    for i,line in enumerate(input):
        idx = i
        if line == "":
            break
        s= line.split("{")
        workflows[s[0]] = s[1].replace("}","").split(",")

    for line in input[idx:]:
        parts.append(line.replace("{","").replace("}","").split(","))
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    #619045 to high
    #495298
    rh = RegexHelper()
    tot = 0
    for part in parts[1:]:
        if evaluate(workflows["in"],part):
            x,m,a,s = rh.extract_numerics_from_list(part)
            tot += x+m+a+s
       
    print("Result First Star")
    print(tot)
  
def second_star():
    rh = RegexHelper()
    ma = 0
    mi = 99999999999
    for x in workflows:
        for idx,i in enumerate(rh.extract_numerics_from_list_as_List(workflows[x])):
            if len(i) and "x" in workflows[x][idx]:
                ma = max(int(i[0]),ma)
                mi = min(int(i[0]),mi)
    print(mi,ma)
    print("Result Second Star")

def evaluate(fu,part):
    rh = RegexHelper()
    x,m,a,s = rh.extract_numerics_from_list(part)
    tot=0
    for ev in fu:
        sp = ev.split(":")
        if len(sp) > 1:
            b=eval(sp[0]) 
            if b:
                if sp[1] == "A":
                    return 1
                
                if sp[1] == "R":
                    return 0
                
                if sp[1] in workflows:
                    return evaluate(workflows[sp[1]],part)
        else:
            if sp[0] == "A":
                return 1
            
            if sp[0] == "R":
                return 0
            
            if sp[0] in workflows:
                    tot+= evaluate(workflows[sp[0]],part)
    return tot   
if __name__ == '__main__':
    main()