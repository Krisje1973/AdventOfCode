import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []
maxx = 0
maxy = 0
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    global maxx
    global maxy
    input = readinput_lines(filename)
    maxx = len(input[0])
    maxy = len(input)
def main():
   readinput("input.txt")
   first_star()       
   second_star()

def first_star():
    result = 0
    antennas = {}
    locations = set()
    for y,line in enumerate(input):
        for x,s in enumerate(line):
            if ord(s) == 46: continue
            if s in antennas.keys():
                antennas[s].append((x,y))
            else: antennas[s] = [(x,y)]

    for antenna in antennas.values():
        for i,pos in enumerate(antenna):
            for j, pos2 in enumerate(antenna[i+1:]):
                diff = add_tuples((-pos[0],-pos[1]),pos2)
                rdiff = (-diff[0],-diff[1])
            
                locations.add(add_tuples(pos,rdiff))
                locations.add(add_tuples(pos2,diff))

    print("Result First Star")
    print(len([0 for r, c in locations if 0 <= r < maxy and 0 <= c < maxx]))

def check_bounderies(pos):
    return 0 <= pos[0] <= maxx and 0 <= pos[1] <= maxy 

def second_star():
    result = 0
    antennas = {}
    locations = set()
    for y,line in enumerate(input):
        for x,s in enumerate(line):
            if ord(s) == 46: continue
            if s in antennas.keys():
                antennas[s].append((x,y))
            else: antennas[s] = [(x,y)]

    for antenna in antennas.values():
        for i,pos in enumerate(antenna):
            for j, pos2 in enumerate(antenna):
                if i == j: continue

                dr,dc = add_tuples((-pos[0],-pos[1]),pos2)
                r,c = pos
                while 0 <= r < maxy and 0 <= c < maxx:
                    locations.add((r, c))
                    r += dr
                    c += dc

    print("Result Second Star")
    print(len(locations))

   
if __name__ == '__main__':
    main()






