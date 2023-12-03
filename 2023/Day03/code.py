import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
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
   
    # 509115
    parts = defaultdict(tuple)
    maxx = len(input[0]) - 1 
    maxy = len(input)
    for y,line in enumerate(input):
        for x in range(len(line)-1):
            c = str(input[y][x])
            if c.isdigit():
                if hasSymbolAsNeighbourg(x,y,maxx,maxy):
                    n,p = getNumAndLastPosition(x,y,line)
                    parts[(y,p)] = n

    print("Result First Star")
    print(sum(parts.values()))

def second_star():
    
    #74254134 low
    #75220503
    parts = defaultdict(tuple)
    maxx = len(input[0]) - 1 
    maxy = len(input)
    tot = 0
    ps = set()
    for y,line in enumerate(input):
        for x in range(len(line)-1):
            c = str(input[y][x])
            if c.isdigit():
                num,_ = getNumAndLastPosition(x,y,line)
                m = getMultiplierLocation(x,y,maxx,maxy) 
                if m != None:
                    ps.add((m,num))
                    if m in parts and parts[m] != num:
                        tot+= num * parts[m]
                    parts[m] = num
 
    print("Result Second Star")
    print(tot)

def getNumAndLastPosition(x,y,line) -> tuple:
    num = ""
    while input[y][x].isdigit() and x!=-1:
        x-=1
    x+=1
    while x!=len(line) and input[y][x].isdigit():
        num+=input[y][x]
        x+=1     

    return int(num),x

def hasSymbolAsNeighbourg(x,y,maxx,maxy):
    gh = GridHelper()
    for nei in gh.get_adjacent_pos_with_diag(x,y,maxx,maxy):
        nx,ny = nei
        if input[ny][nx] != "." and not input[ny][nx].isdigit():
            return True

    return False  

def getMultiplierLocation(x,y,maxx,maxy):
    gh = GridHelper()
    for nei in gh.get_adjacent_pos_with_diag(x,y,maxx,maxy):
        nx,ny = nei
        if input[ny][nx] == "*":
            return (nx,ny)

if __name__ == '__main__':
    main()