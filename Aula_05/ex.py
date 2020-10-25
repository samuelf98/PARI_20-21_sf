#!/usr/bin/env python
# coding=utf-8
import argparse

def main():
        print('Start the game!')
        while True:

            #usage: main.py [-h] [-utm] [-mv MAX_VALUE]

            ap = argparse.ArgumentParser(description='Process some integers.')

            ap = argparse.ArgumentParser(description='Definition of a test mode:')

            ap.add_argument('-utm', '--use_time_mode', action='store_const', const=True,
                            help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.')

            ap.add_argument('-mv', '--max_value', type=int, default=False,
                            help=' Max number of seconds for time mode or maximum number of inputs for number of inputs mode.')
            args=vars(ap.parse_args())
            mv = args['max_value']
            utm = args['use_time_mode']
            if utm==None:
                args['use_time_mode']=False
            print(args)
            break



if __name__ == "__main__":
    main()