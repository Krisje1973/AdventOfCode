import math
import functools ,itertools
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append("C:\DevOpps\GitHub\AdventOfCode")
from  AOCHelper import * 
input = []
def readinput():
    filename = os.path.dirname(__file__) + "\input.txt"
    global input
    input = readinput_as_string(filename)
    
def main():
   readinput()
   first_star()
   second_star()

def find_first_crash(track):
    carts = []
    for y, row in enumerate(track):
        for x, char in enumerate(row):
            if char in ('^', 'v', '<', '>'):
                carts.append(Cart(x, y, char))

    while True:
        # Sort carts by their y, then x coordinates
        carts.sort(key=lambda cart: (cart.y, cart.x))

        for cart in carts:
            cart.move()

            for other_cart in carts:
                if cart != other_cart and cart.x == other_cart.x and cart.y == other_cart.y:
                    return cart.x, cart.y  # Collision found

            track_char = track[cart.y][cart.x]
            cart.turn(track_char)


def first_star():
    print("Result First Star")
 
def second_star():
    print("Result Second Star")
 
if __name__ == '__main__':
    main()

    crash_location = find_first_crash(input)
    print(f"The first crash occurs at location: {crash_location}")
