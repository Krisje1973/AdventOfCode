import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
S = (0,0)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,S
    input = readinput_lines(filename)
    for r,line in enumerate(input):
        for c,s in enumerate(line):
            if s == "S":
                S  = (r,c)
def main():
   readinput("input_ex.txt")
   #first_star()
   second_star()

def first_star():
    plots = deque([S])
    steps = 0
    TH = TupleHelper()
    bound = (len(input)-1,len(input[0])-1)
    while steps < 64:
        np = set()
        while plots:
            plot = plots.pop()
            for step in TH.get_neighbours_with_bounderies(plot,bound):
                if input[step[0]][step[1]] != "#":
                    np.add(step)
        plots = list(np)
        steps+=1

    print("Result First Star")
    print(len(plots))
 
def second_star():
    plots = deque([S])
    steps = 0
    TH = TupleHelper()
    bound = (len(input)-1,len(input[0])-1)
    while steps < 11:
        np = set()
        while plots:
            plot = plots.pop()
            bounds = TH.get_neighbours_with_bounderies(plot,bound)
            if not len(bounds) == 4:
                expand_map()
                bound = (len(input)-1,len(input[0])-1)
                plots.append(())
                bounds = TH.get_neighbours_with_bounderies(plot,bound)
            for step in bounds :
                if input[step[0]][step[1]] != "#":
                    np.add(step)
        plots = list(np)
        steps+=1
   
    print("Result Second Star")
    print(len(plots))
def expand_map():
    global input
    ni = []
    for i in range(1,4):
        for idx,line in enumerate(input):
            if not i % 2:
                nline = line.replace("S",".") + line + line.replace("S",".") 
            else: nline = line.replace("S",".") + line.replace("S",".") + line.replace("S",".")
    
            ni.append(nline)
        
    # gh = GridHelper()
    # print(gh.join_lines_from_list(list(ni)))
    input = ni

if __name__ == '__main__':
    main()