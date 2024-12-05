import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
input = []
updates = []
orders = []
compare = {}

def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    global updates
    global orders
    global compare

    input = readinput_lines(filename)
    orders,updates = FileHelper().get_arrays_from_separator(input,"\n")
    orders = [list(map(int,order.split("|"))) for order in orders]
    updates = [list(map(int,update.split(","))) for update in updates]
   
    for x,y in orders:
        compare[(x,y)] = 1
        compare[(y,x)] = -1

def main():
   readinput("input.txt")
   first_star()       
   second_star()

def first_star():
    result = 0
    for update in updates:
        if isOrdered(update):
            result += update[len(update)//2]

    print("Result First Star")
    print(result)

def isOrdered(update):
    ok = True
    for i,page in enumerate(update):
        # deze mogen niet eerst voorkomen
        after = [b[1] for b in orders if b[0] == page]
        # deze mogen niet later  voorkomen
        before = [b[0] for b in orders if b[1] == page]
        for a in after:
            if len([p for p in update[0:i] if p == a]):
                ok = False

        for b in before:
            if len([p for p in update[i:] if p == b]):
                ok = False
    return ok

def cmp(a,b):
    return compare[(a,b)]

def second_star():
    result = 0
    for update in updates:
        if not isOrdered(update):
            update.sort(key=functools.cmp_to_key(cmp))
            result += update[len(update)//2]
           
    print("Result Second Star")
    print(result)

if __name__ == '__main__':
    main()






