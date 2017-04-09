#!/bin/python2.7

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 

class Pedido(object):

    def __init__(self, cliente="default", b_vermelho=0, b_branco=0, b_preto=0):
        self.cliente = cliente
        self.b_vermelho = b_vermelho
        self.b_branco = b_branco
        self.b_preto = b_preto

    def get_pedido(self):
        return ( self.cliente, self.b_vermelho, self.b_branco, self.b_preto)

    def set_pedido(self, cliente, qtd_b_vermelho, qtd_b_branco, qtd_b_preto):
        self.cliente = cliente
        self.b_vermelho = qtd_b_vermelho
        self.b_branco = qtd_b_branco
        self.b_preto = qtd_b_preto

    def soma_qtd_pecas(self):
        return self.b_vermelho + self.b_branco + self.b_preto

    def mostrar_pedido(self):
        print("%s\t%s\t%s\t%s\n" % ('Cliente', 'Bojos Vermelhos', 'Bojos Brancos', 'Bojos Pretos'))
        print("%s\t%d\t%d\t%d\n" % (self.cliente, self.b_vermelho, self.b_branco, self.b_preto))



if __name__ == '__main__':

    meu_pedido = Pedido()
    meu_pedido.mostrar_pedido()

    meu_pedido = Pedido(cliente='Alan Turing', b_vermelho=500, b_branco=300)
    meu_pedido.mostrar_pedido()
    print( meu_pedido.get_pedido())
