import math
import functools ,itertools
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
   #first_star()
   second_star()

def first_star():
    up_allowed = "S|7F"
    down_allowed = "S|JL"
    right_alowed = "S-7J"
    left_allowed = "S-LF"
    start_pos = []
    for y,line in enumerate(input):
        for x,tile in enumerate(line):
            if tile == "S": 
                start_pos = (y,x)

    loop = {start_pos}
    q = deque([start_pos])

    while q:
        r,c  = q.popleft()
        ch = input[r][c]
        
        # Go up if current Char can go North (up) and receiving char can accept Down (South)
        if r > 0 and ch in down_allowed and input[r - 1][c] in up_allowed and (r - 1, c) not in loop:
            loop.add((r - 1, c))
            q.append((r - 1, c))
            
        if r < len(input) - 1 and ch in up_allowed and input[r + 1][c] in down_allowed and (r + 1, c) not in loop:
            loop.add((r + 1, c))
            q.append((r + 1, c))

        if c > 0 and ch in right_alowed and input[r][c - 1] in left_allowed and (r, c - 1) not in loop:
            loop.add((r, c - 1))
            q.append((r, c - 1))

        if c < len(input[r]) - 1 and ch in left_allowed and input[r][c + 1] in right_alowed and (r, c + 1) not in loop:
            loop.add((r, c + 1))
            q.append((r, c + 1))

    
    print("Result First Star")
    print(len(loop) // 2)

def second_star():
    # 592 to high
    up_allowed = "S|7F"
    down_allowed = "S|JL"
    right_alowed = "S-7J"
    left_allowed = "S-LF"
    start_pos = []
    for y,line in enumerate(input):
        for x,tile in enumerate(line):
            if tile == "S": 
                start_pos = (y,x)

    loop = {start_pos}
    q = deque([start_pos])

    while q:
        r,c  = q.popleft()
        ch = input[r][c]
        
        if r > 0 and ch in down_allowed and input[r - 1][c] in up_allowed and (r - 1, c) not in loop:
            loop.add((r - 1, c))
            q.append((r - 1, c))
            
        if r < len(input) - 1 and ch in up_allowed and input[r + 1][c] in down_allowed and (r + 1, c) not in loop:
            loop.add((r + 1, c))
            q.append((r + 1, c))

        if c > 0 and ch in right_alowed and input[r][c - 1] in left_allowed and (r, c - 1) not in loop:
            loop.add((r, c - 1))
            q.append((r, c - 1))

        if c < len(input[r]) - 1 and ch in left_allowed and input[r][c + 1] in right_alowed and (r, c + 1) not in loop:
            loop.add((r, c + 1))
            q.append((r, c + 1))

if __name__ == '__main__':
    main()