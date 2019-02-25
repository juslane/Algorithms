# Binary Search Algorithm

import random
import numpy as np
import math

COUNT = 0
MIN = 1
MAX = 1

def numbers():
    global MAX
    set_n = input('Numbers will be from 1 to: ')
    MAX = int(set_n)
    max_guesses = np.log2(MAX) + 1
    print('Computer will guess correctly in no more than %d tries!' \
          % math.ceil(max_guesses))

def select_number(disp = True):
    global MIN, MAX, number
    number = random.randint(MIN, MAX)
    if disp == True:
        print('\nComputer Selected: %s\n' % number)

def guess_avg(disp = True):
    global MIN, MAX, avg
    avg = math.floor((MIN + MAX) / 2)
    if disp == True:
        print('Guessing %s\n' % avg)

def high_low():
    global number, avg, MAX, MIN
    if avg > number:
        print('Guess was too high.\n')
        MAX = avg - 1
        main()
    elif avg < number:
        print('Guess was too low.\n')
        MIN = avg + 1
        main()
    else:
        print('You got it! %d is correct!' % number)

def main():
    global COUNT
    COUNT += 1
    print('Guess # %d\n' % COUNT)
    guess_avg()
    high_low()

if __name__ == '__main__':
    numbers()
    select_number()
    main()
