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
    cal = 0
    for line in input:     
        cn = 0
        f = True
        for c in line:
            if c.isdigit():
                cn = int(c)
                if f: 
                    cal+=int(c) * 10
                    f = False
        cal+=cn     

    print("Result First Star")
    print(cal)

def second_star():
    cal = 0
    for line in input:
        s = findStringNumbers(line,True)
        s.extend(findNumbersInString(line,True))
        cal += (min(s)[1] *10) + max(s)[1]
     
    print("Result Second Star")
    print(cal)

if __name__ == '__main__':
    main()