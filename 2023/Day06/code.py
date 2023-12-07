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
    ip = readinput_lines(filename)
    for line in ip:
        line = line.split(":")[1].strip()
        line = list(map(int,line.split()))
        input.append(line)

    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    
    wins = 1
    for idx,time in enumerate(input[0]):
        record =  input[1][idx]
        wins*= len(getRecordBreaking(time,record))
   
    print("Result First Star")
    print(wins)

def second_star():
    time = ""
    record = ""
    for t in input[0]:
        time += str(t)
    for t in input[1]:
        record += str(t)

    
    print(len(getRecordBreaking(int(time),int(record))))
    print("Result Second Star")
 
def getRecordBreaking(time,record):
    result = []
    resttime = time
    speed = 0
    br = False
    for i in range(1,time):
        resttime -= 1
        speed += 1
        if speed*resttime > record:
            br = True
            result.append(i)
        elif br:
            break
            
    return result   

if __name__ == '__main__':
    main()