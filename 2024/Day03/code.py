import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_as_string(filename)
    
def main():
   readinput("input.txt")
   #first_star()       
   second_star()

def first_star():
    result = 0
    for line in input:
        for mul in re.findall(r'mul\([0-9]+,[0-9]+\)', line):
            ins = mul.replace("mul(","").ins.replace(")","").replace(",","*")
            result+= eval(ins)
  
    print("Result First Star")
    print(result)

def second_star():

    result = 0
    idx = 0
    cur = 0
    ins = []
    muls= []
    
    for mul in re.findall(r'mul\([0-9]+,[0-9]+\)', input):
        muls.append(mul.strip())
        ins.append(mul.replace("mul(","").replace(")","").replace(",","*"))
    
    dont = False
    for i,op in enumerate(ins):
        idx = input.rfind(muls[i])

        dont = input[:idx].rfind("don't()") > input[:idx].rfind("do()") and input[:idx].rfind("don't()") >-1
        if not dont : result+= eval(op)
        cur = max(input[cur:idx].rfind("don't()") , input[cur:idx].rfind("do()"))    
           
  
    print("Result Second Star")
    print(result)
   
if __name__ == '__main__':
    main()






