import math
import functools ,itertools
from collections import deque
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
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    dial = 50
    que = deque(i for i in range(100))
    que.rotate(dial)
    answer = 0
    for i in input:                                           
        if i.startswith("L"):
            dial = -int(i[1:])
        else:
            dial = int(i[1:])
        que.rotate(dial)
        answer += que[0] == 0
    print("Result First Star")
    print(answer)
 
def second_star():
    dial = 50
    que = deque(i for i in range(100))
    que.rotate(dial)
    answer = 0
    for i in input:
        dir = -1     
        dial = int(i[1:])                                      
        if i.startswith("L"):
            dir = 1
        for i in range(dial):   
            que.rotate(dir)
            answer += que[0] == 0
    print("Result First Star")
    print(answer)
    print("Result Second Star")
 
if __name__ == '__main__':
    main()