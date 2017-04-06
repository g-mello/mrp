#!/bin/python2.7

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
import Estoque
import Pedido


class Fabrica(object):

    def __init__(self, cidade='São Paulo', estado='SP', tec_vermelho=0, tec_branco=0, tec_preto=0 ):
        self.__cidade = cidade
        self.__estado = estado
        self.__estoque = Estoque.Estoque_MP(tec_vermelho,tec_branco,tec_preto)
        self.pedido = Pedido.Pedido()

    def set_pedido(self, *pedido):
        self.pedido.set_pedido(pedido[0], pedido[1], pedido[2], pedido[3])

    def produzir(self):


        # Quantidade de pedidos por cor
        qtd_b_vermelho = self.pedido.b_vermelho
        qtd_b_branco = self.pedido.b_branco 
        qtd_b_preto = self.pedido.b_vermelho 

        # Quantidade de pedidos levando em consideração a margem de erro
        qtd_v_bojos_margem  = ( qtd_b_vermelho + ( qtd_b_vermelho * 0.1)) 
        qtd_b_bojos_margem  = ( qtd_b_branco + ( qtd_b_branco * 0.1)) 
        qtd_p_bojos_margem  = ( qtd_b_preto + ( qtd_b_preto * 0.1)) 

        
        # Quantidade de pedidos produzidos levando em consideração a
        # quantidade nas placas 
        qtd_v_bojos_produzidos = qtd_v_bojos_margem + ( 8 - ( qtd_v_bojos_margem % 8  ))
        qtd_b_bojos_produzidos = qtd_b_bojos_margem + ( 8 - ( qtd_b_bojos_margem % 8  ))
        qtd_p_bojos_produzidos = qtd_p_bojos_margem + ( 8 - ( qtd_p_bojos_margem % 8  ))

        # Quantidade de placas necessarias 
        qtd_v_placas = ( qtd_v_bojos_produzidos / 8) 
        qtd_b_placas = ( qtd_b_bojos_produzidos / 8) 
        qtd_p_placas = ( qtd_p_bojos_produzidos / 8) 

        #Quantidade de espuma 
        qtd_v_espuma = 1.2 * qtd_v_placas 
        qtd_b_espuma = 1.2 * qtd_b_placas 
        qtd_p_espuma = 1.2 * qtd_p_placas 

        #Quantidade de tecido 
        qtd_v_tecido = 0.4 * qtd_v_placas 
        qtd_b_tecido = 0.4 * qtd_b_placas 
        qtd_p_tecido = 0.4 * qtd_p_placas 

        header0 = "%-10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-10s\t%-10s\n" % ( "","Qtd de Pedido", "Qtd Com Margem de Perda", "Qtd de Peças", "Qtd de Tecido", "Qtd de Espuma", "Qtd de Bojos Produzidos")
        header1 = "%-10s\t%-10d\t%-10d\t%-10d\t%-10.2f\t%-10.2f\t%-10d\n" % ( "Vermelho", qtd_b_vermelho, qtd_v_bojos_margem, qtd_v_placas, qtd_v_tecido, qtd_v_espuma, qtd_v_bojos_produzidos)
        header2 = "%-10s\t%-10d\t%-10d\t%-10d\t%-10.2f\t%-10.2f\t%-10d\n" % ( "Branco", qtd_b_branco, qtd_b_bojos_margem, qtd_b_placas, qtd_b_tecido, qtd_b_espuma, qtd_b_bojos_produzidos)
        header3 = "%-10s\t%-10d\t%-10d\t%-10d\t%-10.2f\t%-10.2f\t%-10d\n" % ( "Preto", qtd_b_preto, qtd_p_bojos_margem, qtd_p_placas, qtd_p_tecido, qtd_p_espuma, qtd_p_bojos_produzidos)

        print(header0)
        print(header1)
        print(header2)
        print(header3)

if __name__ == '__main__':

    meu_pedido = Pedido.Pedido(100, 100, 100)
    meu_pedido.mostrar_pedido()

    minha_fabrica = Fabrica()
    minha_fabrica.set_pedido(*meu_pedido.get_pedido())
    minha_fabrica.produzir()


