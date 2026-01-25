import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
devices = defaultdict(list)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input,devices
    input = readinput_lines(filename)
    for line in input:
        d,c = line.split(":")
        devices[d] = c.split()
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    you = devices['you']

    que = deque()
    que.extend(you)
    result = 0
    while que:
        c = que.pop()
        que.extend(devices[c])
        result += c == 'out'
        
    print("Result First Star")
    print(result)
 
def second_star():
    #371113003846800
   
    result = 0
    serv =  devices['svr']
    que = []
    for c in serv:
        que.append((-1,'',c))
    
    seen = set()
    heapq.heapify(que)
    while que:
        i,s,c = heapq.heappop(que)
        seen.add((s,c))
        if c == 'fft' or c == 'dac':
            if (s == 'fft' and c == 'dac') or (s == 'dac' and c == 'fft'):
                s = "out"

        if c == 'out':
            i+=1
            if s == "out":
                result +=1
        else:        
            for cc in devices[c]:
                if (s,cc) not in seen:
                    que.append((i,c,cc))

    print("Result Second Star")
    print(result)

@cache
def count(src, dst):
    if src == dst: return 1
    return sum(count(x, dst) for x in devices[src])

if __name__ == '__main__':
    main()