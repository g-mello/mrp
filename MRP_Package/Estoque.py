#!/bin/python2.7

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 


class Estoque_MP(object):

    def __init__(self, tec_vermelho=0, tec_branco=0, tec_preto=0, espuma=0.0):
        self.tec_vermelho = tec_vermelho
        self.tec_branco = tec_branco
        self.tec_preto = tec_preto
        self.espuma = espuma

    def get_estoque(self):
        return ( self.tec_vermelho, self.tec_branco, self.tec_preto, self.espuma)

    def set_estoque(self, tec_vermelho, tec_branco, tec_preto, espuma):
        self.espuma = espuma
        self.tec_vermelho = tec_vermelho
        self.tec_branco = tec_branco
        self.tec_preto = tec_preto

    def get_espuma(self):
        return self.espuma

    def mostrar_estoque(self):
        print("%-30s\t%-30s\t%-30s\t%-30s\n" % ("Tecido Vermelho(kg)", "Tecido Branco(kg)", "Tecido Preto(kg)", "Espuma(metros)"))
        print("%-30.2f\t%-30.2f\t%-30.2f\t%-30.2f\n" % (self.tec_vermelho, self.tec_branco, self.tec_preto, self.espuma))

    def mostrar_total(self):
        print("Total em estoque: %d kg\n" %(self.tec_vermelho + self.tec_branco + self.tec_preto))


if __name__ == '__main__':

    meu_estoque = Estoque_MP(10, 10, 10)
    meu_estoque.mostrar_estoque()
    meu_estoque.mostrar_total()

    meu_estoque.set_estoque(20,20,20,10.0)
    meu_estoque.mostrar_estoque()
    meu_estoque.mostrar_total()



