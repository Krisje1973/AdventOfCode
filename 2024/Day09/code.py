import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []
spaces = []
files = []

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    global files
    global spaces
   
    input = list(map(int,readinput_lines(filename)[0]))
    files = [x for i,x in enumerate(input) if i % 2 == 0]
    spaces = [x for i,x in enumerate(input) if i % 2 != 0 and x > 0]
    
def main():
   readinput("input_ex.txt")
   #first_star()       
   second_star()

def first_star():
    result = 0
    ids = len(files) -1
    file_list = [ids-id for id,file in enumerate(files[::-1]) for _ in range(file)]
    empties = [0 for s in spaces for _ in range(s)]   
    for i,_ in enumerate(empties):
        empties[i] = file_list[i]

    empties.reverse()
    end = len(file_list)
    full = []
   
    for i,num in enumerate(input):
        if len(full) == end: break
        if i % 2 == 0:
            for j in range(num):
                full.append(file_list.pop())
        else:
            for j in range(num):
                if len(empties) > 0:    
                    full.append(empties.pop())
                else: full.append(file_list.pop())
   
    print("Result First Star")
    for i,val in enumerate(full[:end]):
        result += i*val
    print(result)

def second_star():
    result = 0
    ids = len(files) -1
    file_list = [ids-id for id,file in enumerate(files[::-1]) for _ in range(file)]
    empties = [0 for s in spaces for _ in range(s)]   
    for i,_ in enumerate(empties):
        empties[i] = file_list[i]

    empties.reverse()
    end = len(file_list)
    full = []
    
    for i,num in enumerate(input):
        if len(full) == end: break
        if i % 2 == 0:
            for j  in range(num):
                full.append(file_list.pop())
        else:
            for j in range(num):
                if len(empties) > 0:    
                    full.append(empties.pop())
                else: full.append(file_list.pop())
    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






