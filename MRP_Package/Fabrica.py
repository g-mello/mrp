#!/bin/python2.7

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
from MRP_Package import Pedido, Estoque

from math import trunc


class Fabrica(object):

    def __init__(self, cidade='São Paulo', estado='SP'):
        self.cidade = cidade
        self.estado = estado
        self.estoque = Estoque.Estoque_MP()
        self.pedido_aberto = list() 
        self.pedido_exec = list() 

    def set_estoque(self, tec_v, tec_b, tec_p, espuma):
        self.estoque.set_estoque(tec_v, tec_b, tec_p, espuma)


    def add_pedido(self, *pedido):
        ''' Adiciona um pedido aos pedidos em aberto '''

        p = Pedido.Pedido(pedido[0], pedido[1], pedido[2], pedido[3])
        self.pedido_aberto.append(p)


    def max_prod(self):
        '''
        Encontra a maxima quantidade de peças que podem ser produzidas
        com a quantidade em atual no estoque
        '''

        ( tec_v, tec_b, tec_p, espuma ) = self.estoque.get_estoque() 
        max_placas = trunc(espuma/1.2 + ( tec_v + tec_b + tec_p)/0.4)
        max_produzidos = max_placas * 8

        return max_produzidos

            
    def __colocar_em_exec(self):
        '''
            Verifica se tem estoque para produzir um pedido em aberto
            inserindo-o em pedidos em execução
        '''
        max_produzidos = self.max_prod()

        for p in self.pedido_aberto:
            qtd_pecas = p.soma_qtd_pecas() 

            if qtd_pecas <= max_produzidos:

                self.pedido_exec.append(p)
                self.pedido_aberto.pop(self.pedido_aberto.index(p))
                    
                max_produzidos -= qtd_pecas


    def produzir(self):
        
        ''' Produz os pedidos na lista de pedidos em execução '''

        self.__colocar_em_exec()

        for p in self.pedido_exec:

            # Quantidade de pedidos por cor
            qtd_b_vermelho = p.b_vermelho
            qtd_b_branco = p.b_branco 
            qtd_b_preto = p.b_preto

            # Quantidade de pedidos levando em consideração a margem de erro
            qtd_v_bojos_margem  = ( qtd_b_vermelho + ( qtd_b_vermelho * 0.1)) 
            qtd_b_bojos_margem  = ( qtd_b_branco + ( qtd_b_branco * 0.1)) 
            qtd_p_bojos_margem  = ( qtd_b_preto + ( qtd_b_preto * 0.1)) 

            
            # Quantidade de pedidos produzidos levando em consideração a
            # quantidade nas placas 
            if qtd_v_bojos_margem > 0:
                qtd_v_bojos_produzidos = qtd_v_bojos_margem + ( 8 - ( qtd_v_bojos_margem % 8  ))
            else:
                qtd_v_bojos_produzidos = 0

            if qtd_b_bojos_margem > 0:
                qtd_b_bojos_produzidos = qtd_b_bojos_margem + ( 8 - ( qtd_b_bojos_margem % 8  ))
            else:
                qtd_b_bojos_produzidos = 0

            if qtd_p_bojos_margem > 0:
                qtd_p_bojos_produzidos = qtd_p_bojos_margem + ( 8 - ( qtd_p_bojos_margem % 8  ))
            else:
                qtd_p_bojos_produzidos = 0


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

            #Dar baixa no estoque
            self.estoque.tec_vermelho -= qtd_v_tecido
            self.estoque.tec_branco -= qtd_b_tecido
            self.estoque.tec_preto -= qtd_p_tecido

            self.estoque.espuma -= ( qtd_v_espuma + qtd_b_espuma + qtd_p_espuma )

            header0 = "%-10s\t%-20s\t%-20s\t%-20s\t%-20s\t%-20s\t%-20s\n" % ( "Cor","Qtd de Pedido", "Qtd Margem de Perda", "Qtd de Peças", "Qtd de Tecido", "Qtd de Espuma", "Qtd de Bojos Produzidos")
            header1 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Vermelho", qtd_b_vermelho, qtd_v_bojos_margem, qtd_v_placas, qtd_v_tecido, qtd_v_espuma, qtd_v_bojos_produzidos)
            header2 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Branco", qtd_b_branco, qtd_b_bojos_margem, qtd_b_placas, qtd_b_tecido, qtd_b_espuma, qtd_b_bojos_produzidos)
            header3 = "%-10s\t%-20d\t%-20d\t%-20d\t%-20.2f\t%-20.2f\t%-20d\n" % ( "Preto", qtd_b_preto, qtd_p_bojos_margem, qtd_p_placas, qtd_p_tecido, qtd_p_espuma, qtd_p_bojos_produzidos)

            print("\nCliente: %s\n" % p.cliente)
            print(header0)
            print(header1)
            print(header2)
            print(header3)


if __name__ == '__main__':

    minha_fabrica = Fabrica()
    minha_fabrica.set_estoque(40,60,50,600)
    print("\nEstoque Inicial\n")
    minha_fabrica.estoque.mostrar_estoque()

    meu_pedido_1 = Pedido.Pedido("Alan Turing", 200, 200, 0)
    meu_pedido_2 = Pedido.Pedido("Bill Gates", 200, 200, 300)
    meu_pedido_3 = Pedido.Pedido("Steve Jobs", 0, 650, 450)

    minha_fabrica.add_pedido(*meu_pedido_1.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_2.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_3.get_pedido())
    minha_fabrica.produzir()

    print("\nEstoque Restante\n")
    minha_fabrica.estoque.mostrar_estoque()





