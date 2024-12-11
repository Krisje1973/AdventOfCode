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
    full = []
    file_list = [(ids-id,file) for id,file in enumerate(files[::-1]) for _ in range(file)]
       
    for i,num in enumerate(input):
        if i % 2 == 0:
            for j  in range(num):
                full.append(file_list.pop())
        else:
            for j in range(num):
                full.append((-1,num))
    new = [file for file in full]            
    for id,le in full[::-1]:
        if id == -1: continue
        #empty = [(i,l) for i,l in full[::-1] if i == -1 and l >= le]
        empty = [(idx,file) for idx,file in enumerate(new) if file[0] == -1 and file[1] >= le]
        if len(empty):
            idx,file = empty[0]
            file = (id,file[1]-le+1)
            new[idx] = file
           # for i in range(le):
            #full.pop(-1)
    print("Result Second Star")
    for i,val in enumerate(new):
        if val[0] > -1:
            result += i*val[0]

    print(new)
    print(result)
    print(len("00...111...2...333.44.5555.6666.777.888899"))
if __name__ == '__main__':
    main()






