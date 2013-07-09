#!/usr/bin/env python
#-*-encoding: utf-8 -*-
from Diamond import Diamond

d = Diamond()
d.printDiamond('E')

"""
Em python os metodos e classe podem ser tratados tambem como estaticos
(nao ha obrigatoriedade de se ter uma instancia do objeto para ter acesso aos atributos metodos)

A proxima instrucao tera o mesmo efeito
"""
#Diamond().printDiamond('w')
