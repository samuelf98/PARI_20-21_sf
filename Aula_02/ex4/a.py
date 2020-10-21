#!/usr/bin/env python
# coding=utf-8


import readchar

def printAllCharsUpTo(stop_char):

    #key = readchar.readkey(c)
    num = ord(stop_char)                #Converte o caracter para decimal
    print('Stop Char: ' + stop_char)
    print('Type char: ')
    str=''
    while True:
        c= readchar.readchar()
        if c == stop_char:
            break
        else:
            print('Try again: ')
    for i in range(32,num+1):                #se começa no '' este cracter em ASCII corresponde ao nº32
            str=str + chr(i)                    #Converte para caracter
    print ('A resposta é:' + str)

def main():
    c = readchar.readchar()
    value = printAllCharsUpTo(c)                    #Vou buscar a string


if __name__ == "__main__":
    main()