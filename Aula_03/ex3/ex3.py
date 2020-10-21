#!/usr/bin/env python
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])


def addComplex(x, y):
    xreal=x.r
    #xreal=x['r']
    xima=x.i

    yreal=y.r
    yima=y.i

    z=complex(xreal+yreal, xima+yima)
    return z
def multiplyComplex(x, y):
    xreal = x.r
    xima = x.i
    x1=complex(xreal,xima)

    yreal = y.r
    yima = y.i
    y1=complex(yreal,yima)

    z=x1*y1
    return z
def printComplex(x):
    print(x)
def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1) +'; c2= '+str(c2)) # named tuple looks nice when printed

    # Test add
    printComplex(addComplex(c1,c2))

    # test multiply
    printComplex( multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()