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
                xmas+= "".join([input[oy][ox] for offset in ne  for ox,oy in offset])
                   
    print("Result First Star")
    print(xmas.count("XMAS"))

def second_star():
    result = 0
    th=TupleHelper()
    dl = [
        (1, -1),  # Diagonaal rechtsonder
        (-1, 1),  # Diagonaal linksboven
    ]
    dr = [
        (1, 1),   # Diagonaal rechtsboven
        (-1, -1),  # Diagonaal linksonder
    ]
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            if col =="A" and y > 0 and y < len(input) -1 and x > 0 and x < len(row) -1:
                xmas = ""
                for d in dl:
                    ox,oy = d
                    ox+=x
                    oy+=y
                    xmas+= input[oy][ox]
                
                ok = (xmas.count("M")and xmas.count("S"))

                xmas = ""
                for d in dr:
                    ox,oy = d
                    ox+=x
                    oy+=y
                    xmas+= input[oy][ox]
                
                result += (xmas.count("M")== 1 and xmas.count("S") == 1) and ok

    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






