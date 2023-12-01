import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 

input = []
valves = {}
tunnels = {}

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    regex = r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$"
    input = re.findall(regex,open_file(filename),re.MULTILINE)
 
    for line in input:
        valve,flow,tunnel = line
        valves[valve] = flow
        tunnels[valve] = [tunnel]
def main():
   readinput("input_ex.txt")
   first_star()
   #second_star()        


def first_star():
   
    visited = set() # Set to keep track of visited nodes of graph.   
    dfs(visited,tunnels,'AA')
    #rint(dag_shortest_path(G,"AA","FF"))
    print("Result First Star")
    

def second_star():
    return "NYI"

    print("Result Second Star")

class Valve():
    def __init__(self, id, rate, tunnels=""):
        self.id:str = id
        self.rate:int = rate
        self.tunnels = {}
        if tunnels != "":
            for tunnel in tunnels.split(", "):
                self.add_tunnel(tunnel)

    def add_tunnel(self,tunnel):
        self.tunnels[tunnel] = Valve(tunnel,0)

if __name__ == '__main__':
    main()