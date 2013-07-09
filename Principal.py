#!/usr/bin/env python
#-*-encoding: utf-8 -*-
from Diamond import Diamond

letra = raw_input("Digite uma letra para fazer a impressao do Diamante: ")

d = Diamond()
d.printDiamond(letra)

"""
Em python os metodos e classe podem ser tratados tambem como estaticos
(nao ha obrigatoriedade de se ter uma instancia do objeto para ter acesso aos atributos metodos)

A proxima instrucao tera o mesmo efeito
"""
#Diamond().printDiamond('w')
