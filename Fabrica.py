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
        self.pedido = list() 

    def add_pedido(self, *pedido):
        p = Pedido.Pedido(pedido[0], pedido[1], pedido[2], pedido[3])
        self.pedido.append(p)

    

    def produzir(self):

        for p in self.pedido:

            # Quantidade de pedidos por cor
            qtd_b_vermelho = p.b_vermelho
            qtd_b_branco = p.b_branco 
            qtd_b_preto = p.b_vermelho 

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

            header0 = "%10s\t%-20s\t%-20s\t%-20s\t%-20s\t%-20s\t%-20s\n" % ( "","Qtd de Pedido", "Qtd Margem de Perda", "Qtd de Peças", "Qtd de Tecido", "Qtd de Espuma", "Qtd de Bojos Produzidos")
            header1 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Vermelho", qtd_b_vermelho, qtd_v_bojos_margem, qtd_v_placas, qtd_v_tecido, qtd_v_espuma, qtd_v_bojos_produzidos)
            header2 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Branco", qtd_b_branco, qtd_b_bojos_margem, qtd_b_placas, qtd_b_tecido, qtd_b_espuma, qtd_b_bojos_produzidos)
            header3 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Preto", qtd_b_preto, qtd_p_bojos_margem, qtd_p_placas, qtd_p_tecido, qtd_p_espuma, qtd_p_bojos_produzidos)

            print(header0)
            print(header1)
            print(header2)
            print(header3)

if __name__ == '__main__':

    meu_pedido_1 = Pedido.Pedido(100, 100, 100)
    meu_pedido_1.mostrar_pedido()

    meu_pedido_2 = Pedido.Pedido(100, 100, 100)
    meu_pedido_2.mostrar_pedido()

    meu_pedido_3 = Pedido.Pedido(100, 100, 100)
    meu_pedido_3.mostrar_pedido()

    minha_fabrica = Fabrica()
    minha_fabrica.add_pedido(*meu_pedido_1.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_2.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_3.get_pedido())

    minha_fabrica.produzir()




