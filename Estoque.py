#!/bin/python2.7

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 


class Estoque_MP(object):

    def __init__(self, tec_vermelho=0, tec_branco=0, tecido_preto=0):
        self.tec_vermelho = tec_vermelho
        self.tec_branco = tec_branco
        self.tec_preto = tecido_preto

    def get_estoque(self):
        return ( self.tec_vermelho, self.tec_branco, self.tecido_preto)

    def set_estoque(self, tec_vermelho, tec_branco, tecido_preto):
        self.tec_vermelho = tec_vermelho
        self.tec_branco = tec_branco
        self.tecido_preto = tecido_preto

    def mostrar_estoque(self):
        print("%-10s\t%-10s\t%-10s\n" % ("Tecido Vermelho(kg)", "Tecido Branco(kg)", "Tecido Preto(kg)"))
        print("%-10s\t%-10s\t%-10s\n" % (self.tec_vermelho, self.tec_branco, self.tec_preto))

    def mostrar_total(self):
        print("Total em estoque: %d kg\n" %(self.tec_vermelho + self.tec_branco + self.tec_preto))


if __name__ == '__main__':

    meu_estoque = Estoque_MP(10, 10, 10)
    meu_estoque.mostrar_estoque()
    meu_estoque.mostrar_total()

    meu_estoque.set_estoque(20,20,20)
    meu_estoque.mostrar_estoque()
    meu_estoque.mostrar_total()



