import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    
def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    junctions = defaultdict(list)
    for idx,line in enumerate(input):
        junctions[idx]= np.array(list(map(int,line.split(','))))

    shortest = []
    boxes = get_all_distances(junctions)
    shortest = sorted(boxes, key=boxes.get)[:1000]  

    dists = []
    for box in find_all_connected(shortest):
        dists.append(len(box))
    dists.sort(reverse=True)
    
    result = 1
    for d in dists[:3]:
        result *= d

    print("Result First Star")
    print(result)

def get_all_distances(junctions):
    boxes = defaultdict(list)
    
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            boxes[(i, j)] = np.linalg.norm(junctions[i] - junctions[j])

    return boxes

def calc_all_distances(junctions,current):
    boxes = defaultdict(list)
    
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            distance = np.linalg.norm(junctions[i] - junctions[j])
            if distance > current:
                boxes[(i, j)] = distance

    shortest = min(boxes, key=boxes.get)
    return shortest, boxes[shortest]

def calc_euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def find_all_connected(pairs):
    # Build an adjacency list from the pairs
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)  # Since the graph is undirected

    # Function to perform BFS and find all connected nodes
    def bfs(start):
        visited = set()
        queue = deque([start])
        connected = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                connected.append(node)
                queue.extend(graph[node])  # Add neighbors to the queue

        return connected

    # Find all connected components
    all_connected = []
    visited_global = set()
    for node in graph:
        if node not in visited_global:
            component = bfs(node)
            all_connected.append(component)
            visited_global.update(component)

    return all_connected

def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()