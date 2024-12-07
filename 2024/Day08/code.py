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
   
    input = readinput_lines(filename)
    
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






