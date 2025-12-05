import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines(filename)[0].split(",")
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()
 
def first_star():
    result = 0
    for id in input:
        s,e = map(int,id.split("-"))
        for i in range(s,e+1):
            s = str(i)
            l = len(s) // 2
            if s[:l] == s[l:]:
                result += i
                
    print("Result First Star")
    print(result)

def second_star():
    result = 0
    rg = RegexHelper()
    for id in input:
        s,e = map(int,id.split("-"))
        for i in range(s,e+1): 
            result += i if rg.has_repeating_pattern(str(i)) else 0

    print("Result Second Star")
    print(result)
if __name__ == '__main__':
    main()