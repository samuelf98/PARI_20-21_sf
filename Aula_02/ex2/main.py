#!/usr/bin/env python3   - ISto foi para usar o shebang
# coding=utf-8
# --------------------------------------------------
# Este código foi retirado da net e compeltado pelo professor RIEM
# Samuel Ferreira
# PARI, Outubro 2020.
# --------------------------------------------------

maximum_number = 100  # maximum number to test.

from my_functions import getDividers, isPerfect
#Do ficheiro my_funcitons importo as funções getDividers e isPerfect

#Se eu quisesse todas as funções desse fciheiro, em vez de só importar essas duas podia fazer:
# import my_functions e depois na linha 21 tinha qeu colocar: my_functions.isPerfect
# ou ainda: import my_functions as mf e depois mf.isPerfect

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')


if __name__ == "__main__":
    main()