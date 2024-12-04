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
    xmas = ""
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            if col =="X":
                ne = TupleHelper().get_neighbours((x,y),3,(len(row),len(input)),NeighbourghType.INCLUDEDIAGONALS)
                xmas+= "".join([input[oy][ox] for ox,oy in ne])
                   
    print("Result First Star")
    print(xmas.count("XMAS"))

def second_star():
    result = 0
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            if col =="A":
                ne = TupleHelper().get_neighbours((x,y),1,(len(row),len(input)),NeighbourghType.ONLYDIAGIONALS,True)
                xmas = "".join([input[oy][ox] for ox,oy in ne])
                result += (xmas[0:2].count("M") == 1 and xmas[0:2].count("S") == 1 and xmas.count("M") == 2 and xmas.count("S") == 2)

    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






