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
   readinput("input_ex.txt")
   #first_star()       
   second_star()

def first_star():
    result = 0
    start = (0,0)
    ch  = Compass()
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            if col == "^": 
                start = (x,y)
    dir = "N"
    maxcol = len(input[0])
    maxrow = len(input)
    seen = set()
    while True:
        move = ch.getHexasPoints(dir)
        x,y  = start
        mx,my = move[0]
        mx+=x
        my+=y
        if mx == -1 or mx == maxcol or my == -1 or my == maxrow:
            break    
        if input[my][mx] == "#":
            dir = ch.turnCompassPoint(dir,"",90)
            continue

        seen.add((mx,my))
        start = (mx,my)
       
    print("Result First Star")
    print(len(seen))

def second_star():
    result = 0
    start = (0,0)
    ch  = Compass()
    for y,row in enumerate(input):
        for x,col in enumerate(row):
            if col == "^": 
                start = (x,y)
    dir = "N"
    maxcol = len(input[0])
    maxrow = len(input)
    seen = set(start)
    cross = 0
    while True:
        move = ch.getHexasPoints(dir)
        x,y  = start
        mx,my = move[0]
        mx+=x
        my+=y
        if mx == -1 or mx == maxcol or my == -1 or my == maxrow:
            break    
        if input[my][mx] == "#":
            dir = ch.turnCompassPoint(dir,"",90)
            cross+=1
            continue

        if (mx,my) in seen:
            cross+=1

        if cross == 4:
            cross = 0
            result+=1      
        seen.add((mx,my))
        start = (mx,my)
   
    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






