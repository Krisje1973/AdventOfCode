import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines_as_int_list(filename)
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    stones = [stone for stone in input[0]]
    for i in range(25):
        blink = []
        for stone in stones:
            if stone == 0: 
                blink.append(1)
            elif len(str(stone)) %2 == 0:
                s = str(stone)
                blink.append(int(s[:len(s)//2]))
                blink.append(int(s[len(s)//2:]))
            else:
                blink.append(stone * 2024)
        stones = [stone for stone in blink]
    print("Result First Star")
    print(len(stones))
 
@cache
def blink(stone,times):
    # run tot 0
    nt = times - 1
    if times == 0:
        return 1

    # Rules
    if stone == 0:
        return blink(1,nt) 
    s = str(stone)
             
    if len(s) %2 == 0:
        return blink(int(s[:len(s)//2]),nt) + blink(int(s[len(s)//2:]),nt)
    
    return blink(2024*stone,nt)

def second_star():
   
    stones = [stone for stone in input[0]]
    
    print("Result Second Star")
    print(sum(blink(stone, 75) for stone in stones))
if __name__ == '__main__':
    main()