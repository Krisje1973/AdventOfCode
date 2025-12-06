import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOps\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput(filename):
    filename = f"{os.path.dirname(__file__)}\{filename}"
    global input
    input = readinput_lines_no_strip_no_enter(filename)
    
def main():
   readinput("input.txt")
   #first_star()
   second_star()

def first_star():
    rh  = RegexHelper()
    nums = {}
    for line in input:
        l = list(rh.extract_numerics(line))
        for idx, n in enumerate(l):
            if idx not in nums:
                nums[idx] = [n]
            else:
                nums[idx].append(n)
    
    result = 0
    op = input[len(input)-1].replace(" ","")
    for l in nums:
        r = 0    
        for n in nums[l]:
            if op[l] == '+' or r == 0:
                r += n
            elif op[l] == '*':
                r *= n
        result += r    

    print("Result First Star")
    print(result)

def second_star():
    # 11090355591833 to high
    
    nums = {}
    for line in input:
        for idx,s in enumerate(line):
            if idx not in nums:
                nums[idx] = s
            else:
                nums[idx] = nums[idx] + s
    nums[max(nums.keys()) + 1] = ' '
    result = 0
#{0: '1  *', 1: '24  ', 2: '356 ', 3: '    ', 4: '369+', 5: '248 ', 6: '8   ', 7: '    ', 8: ' 32*', 9: '581 ', 10: '175 ', 11: '    ', 12: '623+', 13: '431 ', 
#14: '  4 '}
    #{0: [123, 45, 6], 1: [328, 64, 98], 2: [51, 387, 215], 3: [64, 23, 314]}
    
    results=[]
    l = len(nums[0]) -1
    for num in nums:
        results.append((nums[num]))
        if nums[num].strip() == '':
            op = results[0][l]
            r = int(results[0][:l])
            for res in results[1:]:
                if res[:l].strip() == '':
                    continue
                if op == '+' :
                    r += int(res[:l])
                elif op == '*':
                    m = int(res[:l])
                    r *= m
            results=[]  
            
            result += r
         
    print("Result Second Star")
    print(result)
 
if __name__ == '__main__':
    main()