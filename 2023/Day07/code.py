import math
import functools ,itertools
import os, sys
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
cards = defaultdict(int)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)
    for line in input:
        c,b = line.split()
        cards[c] = int(b)

def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    tot = 0
    scores = defaultdict(int)
    for card in cards:
        scores[card] = getScore(card)
   
    scores = dict(sorted(scores.items(), key=lambda x:x[1]))
    sort = defaultdict(str)
    s = "23456789TJQKA"
    r = "abcdefghijklm" 
    for score in scores:
        rs=str(scores[score])
        for c in score:
            rs+= r[s.index(c)]
        sort[score] = rs
    sort = dict(sorted(sort.items(), key=lambda x:x[1]))
    for idx,sor in enumerate(sort):
        tot += cards[sor] * (idx + 1)
        
    print("Result First Star")
    print(tot)

def second_star():
    tot = 0
    scores = defaultdict(int)
    for card in cards:
        scores[card] =  max(map(getScore,getReplacements(card)))
   
    scores = dict(sorted(scores.items(), key=lambda x:x[1]))
   
    sort = defaultdict(str)
    s = "J23456789TQKA"
    r = "abcdefghijklm" 
    for score in scores:
        rs=str(scores[score])
        for c in score:
            rs+= r[s.index(c)]
        sort[score] = rs
    sort = dict(sorted(sort.items(), key=lambda x:x[1]))
    for idx,sor in enumerate(sort):
        tot += cards[sor] * (idx + 1)
        
    print("Result Second Star")
    print(tot)

def getReplacements(card):
    if card == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if card[0] == "J" else card[0])
        for y in getReplacements(card[1:])
    ]


def getScore(card)->int:
    # 7 = Five of a kind,
    ct = Counter(card)
    if len(ct) == 1:
        return 7
    if len(ct) == 2:
        if max(ct.values()) == 4:
            return 6
        else: return 5
    if len(ct) == 3:
        if max(ct.values()) == 3:
            return 4
        else: return 3
    if len(ct) == 4:
        return 2
    
    # High card
    s = "23456789TJQKA"
    idx= s.index(card[0]) 
    for c in card[1::]:
        if s.index(c) != idx+1:
            return 0
        idx = s.index(c)
    
    return 1        

if __name__ == '__main__':
    main()