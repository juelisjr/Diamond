#!/usr/bin/env python
#-*-encoding: utf-8 -*-
class Diamond:

    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    #esta imprimindo do lado inverso (parte de baixo do diamante)?
    isReversed = False
    
    #letra passada por parametro
    letter = None
    
    #quantidade de espacos do lado de fora
    outSpace = None
    
    #quantidade de espacos do lado de dentro - entre as letras
    inSpace = None

    def printDiamond(self, letter):
        """Metodo que ira configurar os atributos e iniciar a impressao do diamante"""

        #transforma a letra passando por parametro em maiuscula
        self.letter = letter.upper()

        #recupera a quantidade inicial de espacos do lado de fora
        #a quantidade de espacos inicial = ao indice da letra no vetor (de letras)
        self.outSpace = 4

        #a quantidade inicial de espacos de dentro (= 0)
        self.inSpace = self.outSpace - self.outSpace

        #depois de configurarmos os atributos, imprimimos linha a linha
        self._printLine()

    def _printLine(self, index = 0):
        """Metodo que imprimira linha a linha do diamante recursivamente"""

        if (index != 0):
            print self.printSpaces(self.outSpace),
            print self.letters[index],
            print self.printSpaces(self.inSpace) + self.letters[index]
        
        else:
            print self.printSpaces(self.outSpace + 1),
            print self.letters[index]
            inSpace = 1

        #enquanto nao encontra a letra no vetor de letras e nao estiver na impressao reversa
        if ((self.letters[index] != self.letter) & (self.isReversed == False)):
            #configura variaveis
            self.outSpace -= 1
            self.inSpace += 2
            index += 1

            #chama o metodo novamante
            self._printLine(index)

        #inicia impressao inversa
        else:
            self.outSpace += 1
            self.inSpace -= 2
            index -= 1
            self.isReversed = True

            #caso base para continuar a impressao inversa
            if(index != -1):
                self._printLine(index)

    def printSpaces(self, quantity):
        """Imprimi os espacos"""
        return " " * quantity
