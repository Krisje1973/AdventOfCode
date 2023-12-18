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
   #second_star()

def first_star():
    beam = Cart(-1,0,">",input)
    print("Result First Star")
    print(len(handle_beam(deque([beam]))))
 
def second_star():
    max_val = 0
    for i in range(len(input)):
        beam = Cart(-1,i,">",input)
        max_val = max(max_val, len(handle_beam(deque([beam])) ))
        beam = Cart(len(input[0]),i,"<",input)
        max_val = max(max_val, len(handle_beam(deque([beam])) ))
        beam = Cart(i,-1,"v",input)
        max_val = max(max_val, len(handle_beam(deque([beam])) ))
        beam = Cart(i,len(input),"^",input)
        max_val = max(max_val, len(handle_beam(deque([beam])) ))

    print("Result Second Star")
    print(max_val)

def handle_beam(beams):
    seen = set()
    while len(beams):
        beam = beams.popleft()
        beam.move()
        if beam.y < 0 or beam.y >= len(input)  or beam.x < 0 or beam.x >= len(input[0]):
            continue
        
        splitted = beam.turn()
        if splitted != None:
            for sp in splitted:
                if (beam.x,beam.y,sp.direction) not in seen:
                    beams.append(sp)
                    seen.add((beam.x,beam.y,sp.direction))
        else: 
            if (beam.x,beam.y,beam.direction) not in seen:
                beams.append(beam)
                seen.add((beam.x,beam.y,beam.direction))
    
    return seen
if __name__ == '__main__':
    main()