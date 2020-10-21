# coding=utf-8
import math

def getDividers(value):


    dividers=[]
    # a raiz pode dar um valor fracionario e o ciclo for apenas dá com nºinteiros
    for i in range(1,int(round(math.sqrt(value)))):
        if (value%i)==0:
            dividers.append(i)
    return dividers


def isPerfect(value):
    """
    Checks whether the number value is perfect.
    :param value: the number to test.
    :return: True or False
    """
    dividers = getDividers(value)
    print('Number ' +str(value) + ' has dividers: ' + str(dividers))

    if not dividers:
        return False
    if sum(dividers)==value:
        return True
    else:
        return False
