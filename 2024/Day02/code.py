import os, sys
from re import Pattern
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
sys.path.append("C:\DevOps\github\AdventOfCode")

from AOCHelper import * 
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
    result = 0
    for line in input:
        l = np.array(list(map(int, line.split())))
        result += check(l)

    print("Result First Star")
    print(result)


def second_star():
    result = 0
    for line in input:
        l = np.array(list(map(int, line.split())))
        if not check(l):
            for i,x in enumerate(l):
                if check(np.delete(l,i)):
                    result+=1
                    break
        else : result+=1
 
    print("Result Second Star")
    print(result)

  
def check(l):
    diff = np.diff(l)
    return (np.all(diff >= 0) or np.all(diff <= 0)) and (np.all(abs(diff) < 4) and np.all(abs(diff)>0))   

if __name__ == '__main__':
    main()






