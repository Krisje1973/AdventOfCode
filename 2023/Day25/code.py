import math
import networkx as nx
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
components = defaultdict(list)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    for line in input:
        c = line.split(":")
        components[c[0]] = c[1].split()
def main():
   readinput("input.txt")
   first_star()
   second_star()



def first_star():
    graph = nx.Graph()
    for comp in components:
        for edge in components[comp]:
            graph.add_edge(comp,edge)
            graph.add_edge(edge,comp)

    
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    a, b = nx.connected_components(graph)

    print("Result First Star")
    print(len(a) * len(b))
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()