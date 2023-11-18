import math
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  AOCHelper import * 
input = []
se,be=[],[]
def readinput():
    global input
    global se,be
    input = readinput_lines("Day15\input.txt")
    
    for s in input:
        se.append((int(s.split("x=")[1].split(",")[0]),int(s.split("y=")[1].split(",")[0].split(":")[0])))
        be.append((int(s.split("x=")[2].split(",")[0]),int(s.split("x=")[2].split(",")[1].split("=")[1])))
   
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    if second_star() != "NYI" : return
    row = 2000000

    # Check if sensor y can reach our row (ook )
        # if so, left, right for as much as Y extends our row 
    pos = {}
    for i,s in enumerate(se):
        m = manhattan(s,be[i])
        x,y = s
        
        if (y>row and y-m <= row) or (y<row and y + m >= row):
            d = m - abs(row-y)
            for j in range(x - d,x+d):
                pos[j] = 1
    
    
    print("Result First Star")
    print(len(pos))
def second_star():
    #return "NYI"


    print("Result Second Star")

if __name__ == '__main__':
    main()