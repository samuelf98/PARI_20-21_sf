#!/usr/bin/env python
import math
from time import time,ctime
from colorama import Fore, Style

def main():

    start = time()

    for i in range(1,50000000):
        x=math.sqrt(i)

    end = time()

    z=end-start
    print('This is Ex1 and the current date is ' + ctime())
    print('Ellapsed time is: ' + Fore.CYAN + str(z) + Style.RESET_ALL)

if __name__ == "__main__":
    main()
