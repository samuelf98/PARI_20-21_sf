# coding=utf-8
def getDividers(value):
    #Em cima da função carregar alt+enter > Insert Documentation String
    """ Aqui escrevo o que a função faz

    :param value: explico o que os parâmetros são. Neste caso este é o de entrada
    :return: Outro parâmtro, neste caso de saída
    """
    dividers=[]
    for i in range(1,value):
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

    if not dividers:        #se a lista estiver vazia (siginivida que não é perfeito)
        return False
    if sum(dividers)==value:
        return True
    else:
        return False
