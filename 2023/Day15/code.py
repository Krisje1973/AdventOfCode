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
    input = input[0].split(",")
def main():
    readinput("input.txt")
    first_star()
    second_star()

def first_star():
    print("Result First Star")
    print(sum(map(hash,input)))
 
def second_star():
    boxes = defaultdict(dict)
    for i in range(256):
        boxes[i] = {}

    for h in input:
        op = "=" 
        if "-" in h:
            op = "-"
        label,focal = h.split(op)
        box = hash(label)
        if op == "-":
            if label in boxes[box]:
                boxes[box].pop(label,None)
            continue

        boxes[box][label] = focal
   
    tot = 0
    for b,box in enumerate(boxes):
        for l,lens in enumerate(boxes[b]):
            tot += ((b + 1) * (l + 1)) * int(boxes[b][lens])

    print("Result Second Star")
    print(tot)
def hash(s) -> int:
    tot=0
    for c in s:
        tot=((tot+ord(c))* 17) % 256

    return tot
if __name__ == '__main__':
    main()