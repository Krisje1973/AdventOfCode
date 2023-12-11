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
    input = readinput_lines(filename)
    
def main():
   readinput("input_ex.txt")
   first_star()
   second_star()

def addidtion(fish):
    return [addidtion]
    
def explode_first_rule(fish):
    #nested in four pairs: the leftmost such pair explodes.
    #If any regular number is 10 or greater, the leftmost such regular number splits.

    #[[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular number to its left, so it is not added to any regular number).
    #[7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular number to its right, and so it is not added to any regular number).
    #[[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
    #[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the pair [7,3] is further to the left; 
    #   [3,2] would explode on the next action).
    #[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
    sp = []
    sp = fish.replace("[","|").replace("]","|").split("|")
    
    print(sp)
    
        
    #If any regular number is 10 or greater, the leftmost such regular number splits.
def first_star():
    explode_first_rule(input[1])
    print("Result First Star")
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()