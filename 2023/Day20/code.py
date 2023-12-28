import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
modules = defaultdict(str)
broadcaster = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,modules,broadcaster
    input = readinput_lines(filename)
    for line in input:
        op,de = line.split("->")
        op = op.strip().lstrip()
        de = list(map(strips,de.split(",")))          
        if op.startswith("broadcaster"):
            broadcaster = de
        else:
            modules[op[1:]] = Module(op[0],de)
        
    print(modules)
def main():
   readinput("input_ex.txt")
   first_star()
   second_star()

def first_star():
    for     
    
    print("Result First Star")
 
def second_star():
    print("Result Second Star")

def strips(s):
    return s.lstrip().strip()

class Module:
    def __init__(self,type,outputs):
        self.outputs = outputs
        self.type = type
        if type == "%":
            self.state = False
        else: self.state = {}
         
if __name__ == '__main__':
    main()