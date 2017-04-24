#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
import Pedido, Estoque

from math import trunc
import random
import sqlite3


class Fabrica(object):

    def __init__(self, cidade='Sao Paulo', estado='SP'):
        
        self.id_fabrica=random.randint(0,100)
        self.cidade = cidade
        self.estado = estado
        self.estoque = Estoque.Estoque_MP(id_fabrica=self.id_fabrica)
        self.pedido_aberto = list() 
        self.pedido_exec = list() 

        self.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                                INSERT INTO tb_fabrica(id_fabrica,cidade,estado)
                                VALUES
                                (?,?,?)
                            ''', (self.id_fabrica, self.cidade, self.estado)
                           )

        self.conn.commit()


    def set_estoque(self, tec_v, tec_b, tec_p, espuma):
        self.estoque.set_estoque(tec_v, tec_b, tec_p, espuma)


    def add_pedido(self, pedido):
        ''' Adiciona um pedido aos pedidos em aberto '''
        #p = Pedido.Pedido(pedido[0], pedido[1], pedido[2], pedido[3])
        self.pedido_aberto.append(pedido)


    def max_prod(self):
        '''
        Encontra a maxima quantidade de pecas que podem ser produzidas
        com a quantidade em atual no estoque
        '''

        ( tec_v, tec_b, tec_p, espuma ) = self.estoque.get_estoque()[2:] 
        max_placas = trunc(espuma/1.2 + ( tec_v + tec_b + tec_p)/0.4)
        max_produzidos = max_placas * 8

        return max_produzidos

            
    def __colocar_em_exec(self):
        '''
            Verifica se tem estoque para produzir um pedido em aberto
            inserindo-o em pedidos em execucao
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

        dados_producao = list()
        pedidos_producao = list()
        dados_totais = list()

        for p in self.pedido_exec:

            pedidos_producao.append(Pedido.Pedido.get_pedido(p.id_cliente))

            # Quantidade de pedidos por cor
            qtd_b_vermelho = p.qtd_b_vermelho
            qtd_b_branco = p.qtd_b_branco 
            qtd_b_preto = p.qtd_b_preto

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
            self.estoque.qtd_tec_vermelho -= qtd_v_tecido
            self.estoque.qtd_tec_branco -= qtd_b_tecido
            self.estoque.qtd_tec_preto -= qtd_p_tecido
            self.estoque.qtd_espuma -= ( qtd_v_espuma + qtd_b_espuma + qtd_p_espuma )

            self.estoque.set_estoque(self.estoque.qtd_tec_vermelho,
                                     self.estoque.qtd_tec_branco,
                                     self.estoque.qtd_tec_preto,
                                     self.estoque.espuma)

            print("DEBUG << baixa no estoque >>")
            print("Qtd_Tec_Verm: ", qtd_v_tecido )
            print("Qtd_Tec_Branco: ", qtd_b_tecido )
            print("Qtd_Tec_Preto: ", qtd_b_preto)
            print("Qtd Espuma: ", ( qtd_v_espuma + qtd_b_espuma + qtd_p_espuma ))


            #Marcar pedido como realizado no banco de dados
            p.cursor.execute('''
                                UPDATE tb_pedido
                                SET fg_ativo = 0 
                                WHERE id_pedido = ?
                             ''', (p.id_pedido,)
                    )

            p.conn.commit()

            dados_producao.append([
                                   qtd_b_vermelho + qtd_b_branco + qtd_b_preto, 
                                   qtd_v_bojos_margem + qtd_b_bojos_margem + qtd_p_bojos_margem, 
                                   qtd_v_placas + qtd_b_placas + qtd_p_placas, 
                                   qtd_v_tecido + qtd_b_tecido + qtd_p_tecido, 
                                   qtd_v_espuma + qtd_b_espuma + qtd_v_espuma , 
                                   qtd_v_bojos_produzidos + qtd_b_bojos_produzidos + qtd_p_bojos_produzidos
                                 ])
        
        dados_totais.append(pedidos_producao)    
        dados_totais.append(dados_producao)    

        return dados_totais 



if __name__ == '__main__':

    minha_fabrica = Fabrica()
    minha_fabrica.set_estoque(40,60,50,600)
    print("\nEstoque Inicial\n")
    minha_fabrica.estoque.mostrar_estoque()

    meu_pedido_1 = Pedido.Pedido(1,1,500,300,0)
    meu_pedido_2 = Pedido.Pedido(2,2,200,200,300)
    meu_pedido_3 = Pedido.Pedido(3,3,400,650,0)

    minha_fabrica.add_pedido(meu_pedido_1)
    minha_fabrica.add_pedido(meu_pedido_2)
    minha_fabrica.add_pedido(meu_pedido_3)
    minha_fabrica.produzir()

    print("\nEstoque Final\n")
    minha_fabrica.estoque.mostrar_estoque()






