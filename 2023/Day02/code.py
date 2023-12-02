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
    games = {}
    reg = RegexHelper() 
    valid = 0
    for line in input:
        spl = line.split(":")
        game = reg.extract_numerics(spl[0])[0]
        games[game] = {}
        isValid = True
        for sp in spl[1].split(";"):
            s = sp.split(",")
            games[game] = {}
            for ss in s:
                cubes = ss.split()
                 
                if cubes[1] in games[game]:
                    games[game][cubes[1]] += int(cubes[0])
                else: games[game][cubes[1]] = int(cubes[0])
            
            red,blue,green = 0,0,0

            if "red" in games[game] : red += games[game]["red"]
            if "blue" in games[game] : blue += games[game]["blue"]   
            if "green" in games[game] : green += games[game]["green"]

            if not( red <= 12 \
            and green <= 13 \
            and blue <= 14):
                isValid = False

        if isValid: valid += game     
      
    # only 12 red cubes, 13 green cubes, and 14 blue cubes?
    # 2085
    print("Result First Star")
    print(valid)
  
def second_star():
    games = {}
    reg = RegexHelper() 
    valid = 0
    for line in input:
        spl = line.split(":")
        game = reg.extract_numerics(spl[0])[0]
        games[game] = {}
      
        maxRed,maxBlue,maxGreen = 0,0,0
        for sp in spl[1].split(";"):
            s = sp.split(",")
            games[game] = {}
           
            for ss in s:
                cubes = ss.split()
                 
                if cubes[1] in games[game]:
                    games[game][cubes[1]] += int(cubes[0])
                else: games[game][cubes[1]] = int(cubes[0])
            
            red,blue,green = 0,0,0

            if "red" in games[game] : red += games[game]["red"]
            if "blue" in games[game] : blue += games[game]["blue"]   
            if "green" in games[game] : green += games[game]["green"]

            if red > maxRed: maxRed = red
            if blue > maxBlue: maxBlue = blue
            if green > maxGreen: maxGreen = green   
        
        valid += maxRed * maxBlue * maxGreen

    print("Result Second Star")
    print(valid)
if __name__ == '__main__':
    main()