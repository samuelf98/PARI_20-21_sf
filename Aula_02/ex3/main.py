#!/usr/bin/env python
# coding=utf-8
#linha 1 foi para usar o shebang. Agora no terminal posso colocar "./main.py --maximum_number 10"    ou outro nº qualquer
import argparse



#Quero utilizar um argumento de entrada. neste caso o valor máximo que quero testar se são primos. Uso o argparse (linha 14)


from my_functions import getDividers, isPerfect

def main():
    ap = argparse.ArgumentParser(description='Process some integers.')
    ap.add_argument('-mn', '--maximum_number', type=int, default=20,
                        help='Maximum Number to evaluate:')

    args=vars(ap.parse_args())
    print(args)
    maximum_number=args['maximum_number']


    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()