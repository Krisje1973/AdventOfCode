import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []
update = []
order = []


def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    global update
    global order

    input = readinput_lines(filename)
    o = True
    for line in input:
        if len(line) == 0:
            b = False
            continue
        if b:
            order.append(line)
        else:
            update.append(line)
    print(order)
    
def main():
   readinput("input.txt")
   first_star()       
   second_star()

def first_star():
    result = 0
  
    print("Result First Star")
    print(result)

def second_star():
    result = 0
   
    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






