import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\Devops\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    result = 0
    for line in input:
        h1 = max(map(int, re.findall(r'(\d)(?=\d)', line)))
        rest = line[line.index(str(h1))+1:] 
        h2 = max(map(int, rest))
        result += h1 * 10 + h2
    print("Result First Star")
    print(result)
 
def second_star():
    result = 0
    for line in input:
       result += get_highest_digit_number(line,12)
     
    print("Result Second Star")
    print(result)



if __name__ == '__main__':
    main()