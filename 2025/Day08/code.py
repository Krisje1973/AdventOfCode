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
   #first_star()
   second_star()

def first_star():
    junctions = defaultdict(list)
    for idx,line in enumerate(input):
        junctions[idx]= np.array(list(map(int,line.split(','))))

    shortest = []
    boxes = get_all_distances(junctions)
    shortest = sorted(boxes, key=boxes.get)[:10]  

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
            boxes[(i, j)] = calc_euclidean_distance(junctions[i] , junctions[j])

    return boxes

def second_star():
    result = 0
    junctions = defaultdict(list)
    for idx,line in enumerate(input):
        junctions[idx]= list(map(int,line.split(',')))
    
    boxes = get_all_distances(junctions)
    boxes = sorted(boxes, key=boxes.get)
    for box in boxes:
        a,b = box
        
        junctions = removekeyfromdict(junctions,a)
        junctions = removekeyfromdict(junctions,b)
       
        if len(junctions) == 0:
            for idx,line in enumerate(input):
                junctions[idx]= list(map(int,line.split(',')))
            result = junctions[a][0] * junctions[b][0]
            break


    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()