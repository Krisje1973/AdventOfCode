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
                    xn = x
                    num = ""
                    while input[y][xn].isdigit() and xn!=-1:
                        xn-=1
                    xn+=1
                    while xn!=len(line) and input[y][xn].isdigit():
                        num+=input[y][xn]
                        xn+=1     
                   
                    parts[(y,xn)] = int(num)

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
                # get number
                xn = x
                num = ""
                while input[y][xn].isdigit() and xn!=-1:
                    xn-=1
                xn+=1
                while xn!=len(line) and input[y][xn].isdigit():
                    num+=input[y][xn]
                    xn+=1     
                
                num=int(num)
                m = getMultiplierLocation(x,y,maxx,maxy) 
                if m != None:
                    ps.add((m,num))

    for p in ps:
        if p[0] in parts:
            tot+= p[1] * parts[p[0]]
        parts[p[0]] = p[1]

    print("Result Second Star")
    print(tot)

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