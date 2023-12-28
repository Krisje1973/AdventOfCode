import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
end = 0
seen = set()
points = defaultdict(list)
visitedList = [[]]
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    
def main():
   readinput("input_ex.txt")
   first_star()
   second_star()

def first_star():
    global end,seen,points,visitedList
    start = (0, input[0].index("."))
    end = (len(input) - 1, input[-1].index("."))
  
    TH = TupleHelper()
    movements = {"^":(-1,0),"v":(1,0),"<":(0,-1),">":(0,1)}
    crossroads = [start,end]
    for r, row in enumerate(input):
        for c, ch in enumerate(row):
            if ch == "#":
                continue       
            nei = 0    
            for nr, nc in TH.get_neighbours_with_bounderies((r,c),(len(input)-1,len(input[0])-1)):
                nch = input[nr][nc]
                if nch == ".": 
                    points[(r,c)].append((nr, nc))
                    nei += 1
                if nch in movements: 
                    points[(r,c)].append(TH.add_tuples((nr, nc),movements[nch]))
                    nei += 1
            if nei >= 3:
                crossroads.append((r,c))
    paths = []
    graph = Graph(points)
    tot=0
    se = defaultdict(int)
    for cross in crossroads[2:]:
        m = 0
        crosspath = graph.find_all_paths(start,cross)
        for i in crosspath:
            m = max(m,len(i))
        se[cross] = m
        m = 0
        crosspath = graph.find_all_paths(cross,end)
        for i in crosspath:
            m = max(m,len(i))
        se[cross] = se[cross] + m

    print("Result First Star")
    print(se)
 
def second_star():
    print("Result Second Star")

def dfs(graph, currentVertex, visited):
    visited.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            dfs(graph, vertex, visited.copy())
        visitedList.append(visited) 

   
if __name__ == '__main__':
    main()