#!/usr/bin/env python
#-*-encoding: utf-8 -*-


class Diamond:


    __letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #esta imprimindo do lado inverso (parte de baixo do diamante)?
    __isReversed = False

    #letra passada por parametro
    __letter = None

    #quantidade de espacos do lado de fora
    __outSpace = None

    #quantidade de espacos do lado de dentro - entre as letras
    __inSpace = None

    def printDiamond(self, letter):
        """Metodo que ira configurar os atributos e iniciar a impressao do diamante"""

        #transforma a letra passando por parametro em maiuscula
        self.__letter = letter.upper()

        #recupera a quantidade inicial de espacos do lado de fora
        #a quantidade de espacos inicial = ao indice da letra no vetor (de letras)
        self.__outSpace = 4

        #a quantidade inicial de espacos de dentro (= 0)
        self.__inSpace = self.__outSpace - self.__outSpace

        #depois de configurarmos os atributos, imprimimos linha a linha
        self.__printLine()

    def __printLine(self, index=0):
        """Metodo que imprimira linha a linha do diamante recursivamente"""

        if (index != 0):
            print self.__printSpaces(self.__outSpace),
            print self.__letters[index],
            print self.__printSpaces(self.__inSpace) + self.__letters[index]

        else:
            print self.__printSpaces(self.__outSpace + 1),
            print self.__letters[index]
            #inSpace = 1

        #enquanto nao encontra a letra no vetor de letras e nao estiver na impressao reversa
        if ((self.__letters[index] != self.__letter) & (self.__isReversed is False)):
            #configura variaveis
            self.__outSpace -= 1
            self.__inSpace += 2
            index += 1

            #chama o metodo novamante
            self.__printLine(index)

        #inicia impressao inversa
        else:
            self.__outSpace += 1
            self.__inSpace -= 2
            index -= 1
            self.__isReversed = True

            #caso base para continuar a impressao inversa
            if(index != -1):
                self.__printLine(index)

    def __printSpaces(self, quantity):
        """Imprimi os espacos"""
        return " " * quantity
