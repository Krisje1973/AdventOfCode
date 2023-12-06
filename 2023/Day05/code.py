import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
seeds = []
categories = []
ranges = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,seeds,categories,ranges
    input = readinput_lines(filename)
    seeds = list(map(int,input[0].split(":")[1].split()))
    newcat = False
    subCat = Category(None)
    cat = None
    
    for line in input[2::]:
        if len(line) == 0:
            continue
        if ":" in line:
            newcat = True
            continue

        if newcat : 
            cat = Category(cat)
            categories.append(cat)
            if len(categories) >= 2:
                categories[-2].subCategory = cat
        newcat = False
        if cat != None : subCat = cat
        
        dest,source,lenrange = map(int,line.split())
        cat.dest.append(int(dest))
        cat.source.append(int(source))
        cat.lenrange.append(int(lenrange))

        ranges.append((dest,source,lenrange))

   
    # cat = Category(None)
    

    # soils = Category(None)
    # soils.dest.append(52)
    # soils.source.append(50)
    # soils.lenrange.append(48)

    # print(soils.getDestination(53))
    #0.0 <= x <= 0.5


class Category:
    def __init__(self,subCat):
        self.dest = []
        self.source = []
        self.lenrange = [] 
        self.subCategory = Category
        self.subCategory = subCat

    def getDestination(self,source):  
        for idx,d in enumerate(self.source):
            if d <= source <= d+self.lenrange[idx]:
                return self.dest[idx]+(source-d)
        return source

    

def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    locs = []
    for seed in seeds:
        soil = categories[0].getDestination(seed)
        fert = categories[1].getDestination(soil)
        water = categories[2].getDestination(fert)
        light = categories[3].getDestination(water)
        temp = categories[4].getDestination(light)
        hum = categories[5].getDestination(temp)
        locs.append(categories[6].getDestination(hum))

           
    print("Result First Star")
    print(min(locs)) 

def second_star():
    global seeds
   
    r = []
    for idx,_ in enumerate(seeds):
        if idx % 2:
            r.append((seeds[idx-1],seeds[idx-1]+seeds[idx]))
    seeds = r
    for cat in categories:
        ranges = []
        for idx,d in enumerate(cat.dest):
            ranges.append([d,cat.source[idx],cat.lenrange[idx]])
       
        nextcat = []
        for start,end in seeds:
            for dest, source, length in ranges:
                maxs = max(start, source)
                mine = min(end, source + length)
                if maxs < mine:
                    nextcat.append((maxs - source + dest, mine - source + dest))
                    if maxs > start:
                        seeds.append((start, maxs))
                    if end > mine:
                        seeds.append((mine, end))
                    break
            else:
                nextcat.append((start, end)) # No location found
  
        seeds = nextcat

    print("Result Second Star")
    print(min(seeds)[0])
           
  
if __name__ == '__main__':
    main()