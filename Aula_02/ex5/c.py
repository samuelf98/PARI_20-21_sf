#!/usr/bin/env python
# coding=utf-8


import readchar


def printAllCharsUpTo(stop_char):
    print('Stop Char: ' + stop_char)
    print('Typed char: ')
    string=''
    while True:
        c = readchar.readchar()
        string=string+str(c)
        if c == stop_char:
            return readAllUpTo(c,string)
        else:
            print('Try again: ')


def readAllUpTo(stop_char,string):
    num = ord(stop_char)
    str = ''
    for i in range(32, num + 1):  # se começa no '' este cracter em ASCII corresponde ao nº32
        str = str + chr(i)  # Converte para caracter
    print ('A resposta é:' + str)
    return countNumbersUpto(stop_char,string)


def countNumbersUpto(stop_char,string):
    total_numerics = 0
    num = ord(stop_char)
    stop=0
    inputs=string
    digitos_inseridos=0
    caracteres_ins=0
    lista=[]

    #Dicionário
    #thisdictionary[key] = value

    thisdictionary= {}

    while True:
        for input in inputs:

            if input.isdigit():
                digitos_inseridos=digitos_inseridos+1
                lista.append(input)
            else:
                caracteres_ins=caracteres_ins+1
                thisdictionary[caracteres_ins] = input

        for i in range(32, num + 1):
            x = chr(i)
            if x.isdigit():
                total_numerics = total_numerics + 1
            if i == num:
                total_others = num - total_numerics - 32
                stop=1                  #Variável apenas para parar o ciclo while
                print('You entered ' + str(total_numerics) + ' numbers;' + ' Numeric Inputs: ' + str(digitos_inseridos) + '; Lista: ' + str(lista))
                print('You entered ' + str(total_others) + ' others,;' + ' Character Inputs: ' + str(caracteres_ins) + '.')
                print(thisdictionary)
        if stop==1:
            break


def main():
    c = readchar.readchar()
    value = printAllCharsUpTo(c)  # Vou buscar a string


if __name__ == "__main__":
    main()
