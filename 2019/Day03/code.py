import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
def readinput():
    filename = os.path.dirname(__file__) + "\input.txt"
    global input
    input = readinput_lines(filename)
    
def main():
   readinput()
   first_star()
   second_star()

def first_star():
    print("Result First Star")
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()