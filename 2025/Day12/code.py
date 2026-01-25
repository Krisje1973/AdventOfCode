import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
shapes = defaultdict(list)
regions = defaultdict(list)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input, shapes,regions
    input = readinput_as_pairs(filename)
    shape = ""
    for line in input:
        k,v = line[0].split(":")
        if not v and k != shape :
            shape = k
        if "x" in k:
            i = 0
            regions[i].append([k,v])
            for r in line[1:]:
                i+=1
                k,v = r.split(":")
                regions[i].append([k,v])
        else:
            shapes[int(shape)].extend(line[1:])
    
    assert len(shapes)==6, "Shapes count is not 6"
    
def main():
   readinput("input_ex.txt")
   #first_star()
   second_star()

def first_star():
    result = 0
    for k,v in regions.items():
        for r in v:
            x,y = map(int,r[0].split('x'))
            total  = sum(map(int, r[1].split())) 
            if (x//3)*(y//3) >= total:
                result+=1

    print("Result First Star")
    print(result)

def second_star():
    sh = ShapeHelper()
    gh = GridHelper()
    result = 0
    for k,v in regions.items():
        for r in v:
            x,y = map(int,r[0].split('x'))
            presents = []
            for sh,num in enumerate(list(map(int, r[1].split()))):
                if not num: continue
                for i in range(num):
                    presents.append(ShapeHelper(grid=shapes[sh]))

            region = gh.get_grid(x,y)
            for present in presents:
                # 7 rotates

                if check_region(list(region),presents): result += 1

            
            print(presents[0].coordinates)

    print("Result Second Star")
    print(result)


def check_region(region,shapes):
    for shape in shapes:
        for coord in shape.coordinates:
            try:
                region.remove(coord)
            except ValueError as e:
                return False 
    return True
if __name__ == '__main__':
    main()