#!/usr/bin/env python
# coding=utf-8


import readchar


def printAllCharsUpTo(stop_char):
    print('Stop Char: ' + stop_char)
    print('Typed char: ')
    while True:
        c = readchar.readchar()
        if c == stop_char:
            return readAllUpTo(c)
        else:
            print('Try again: ')


def readAllUpTo(stop_char):
    num = ord(stop_char)
    str = ''
    for i in range(32, num + 1):  # se começa no '' este cracter em ASCII corresponde ao nº32
        str = str + chr(i)  # Converte para caracter
    print ('A resposta é:' + str)
    return countNumbersUpto(stop_char)


def countNumbersUpto(stop_char):
    total_numbers = 0
    num = ord(stop_char)
    stop=0
    while True:
        for i in range(32, num + 1):
            x = chr(i)
            if x.isdigit():
                total_numbers = total_numbers + 1
            if i == num:
                total_others = num - total_numbers - 32
                stop=1                  #Variável apenas para parar o ciclo while
                print('You entered ' + str(total_numbers) + ' numbers.')
                print('You entered ' + str(total_others) + ' others.')
        if stop==1:
            break
def main():
    c = readchar.readchar()
    value = printAllCharsUpTo(c)  # Vou buscar a string


if __name__ == "__main__":
    main()
