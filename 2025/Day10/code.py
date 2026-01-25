import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
machines = defaultdict(list)
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input, machines
    input = readinput_lines(filename)
    B = Binary()
    for line in input:
        ls = line.split()
        machine = remove_first_last(ls.pop(0)).replace("#",'1').replace(".","0")
        _ = ls.pop(-1)
        machines[machine] = ls
    for machine in machines:
        buttons = []
        for button in machines[machine]:
            for b in getDigitsFromString(button):
                buttons.append(B.generate_binary_string(len(machine),b))
        machines[machine] = buttons
        
def remove_first_last(line):
    return line[1:-1]
    #output_string = re.sub(r"[\[\]]", "", line)        

def main():
   readinput("input.txt")
   first_star()
   second_star()

def first_star():
    result = 0
    B = Binary()
    for machine in machines:
        for i in range(1,len(machines[machine]) + 1):
            for button in itertools.combinations(machines[machine], i):
                lights = "".zfill(len(machine))
                for b in button:
                    lights = B.get_binary_as_string(int(lights, 2) ^ int(b, 2),len(machine))
                   
                if lights == machine:
                    result += i
                    break
            else:
                continue
            break
    
    print("Result First Star")
    print(result)
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()