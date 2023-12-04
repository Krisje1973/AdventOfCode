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
    tot=0
    for line in input:
        win,cards = line.split("|")
        win = win.split()[2::]
        cards = cards.split()
        ct=0
        for w in win:
            if w in cards:
                if ct == 0:
                    ct = 1
                else : ct = ct * 2
        tot+=ct
    print("Result First Star")
    print(tot)

def second_star():
    # 12847 low
    # 8467762
    newcards = defaultdict(list)
    tot = 0
    for idx,line in enumerate(input):
        currCardNo = line.split()[1].split(":")[0]
        cards = processLine(line,idx)
        
        for card in cards:
            cardNo = card.split()[1].split(":")[0]
            for _ in range(len(newcards[currCardNo])):
                newcards[cardNo].append(card)
            newcards[cardNo].append(card)

    for card in newcards:
        tot+= len(newcards[card])

    print("Result Second Star")
    print(tot + len(input))

def processLine(line,lineNo)->list:
    result = []
    win,cards = line.split("|")
    
    win = win.split()[2::]
    cards = cards.split()
    ct=0
    for w in win:
        if w in cards:
            ct+= 1

    lineNo += 1
    for line in input[lineNo:lineNo+ct]:
        result.append(line)
    
    return result
if __name__ == '__main__':
    main()