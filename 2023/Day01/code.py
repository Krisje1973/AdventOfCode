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
    print("Result First Star")
    cal = 0
    for line in input:
        cn = 0
        f = True
        for c in line:
            if c.isnumeric():
                cn = int(c)
                if f: 
                    cal+=int(c) * 10
                    f = False
        cal+=cn     
    print(cal)
def second_star():
    cal = 0
    for line in input:
        s = findStringNumbers(line)
        s.extend(findNumbersInString(line))
        cal += (min(s)[1] *10) + max(s)[1]
     
    print("Result Second Star")
    print(cal)

def findStringNumbers(s):
    results = []
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    for i,num in enumerate(numbers):
        p=0
        s2=s
        while s2.find(num)>-1:
            p+=s2.index(num)
            results.append((p,i+1))
            p+=1
            s2 = s[p::]

    return results;

def findNumbersInString(s):
    results = []
    for i,num in enumerate(s):
        if(num.isdigit()):
            results.append((i,int(num)))

    return results;

if __name__ == '__main__':
    main()