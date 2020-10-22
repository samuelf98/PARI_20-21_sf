#!/usr/bin/env python
# coding=utf-8
import argparse

def main():
        print('Start the game!')
        while True:

            #usage: main.py [-h] [-utm] [-mv MAX_VALUE]

            ap = argparse.ArgumentParser(description='Process some integers.')
            ap.add_argument('-mn', '-maximum_number', type=int, default=20,
                                help='Maximum Number to evaluate:')
            ap.add_argument('-mv', '--teste', type=int, default=20,
                                help='Maximum Number to evaluate:')
            args=vars(ap.parse_args())

            print(args)
            break



if __name__ == "__main__":
    main()