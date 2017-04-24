#!/usr/bin/env python

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
import sqlite3

class Pedido(object):

    def __init__(self, id_cliente, b_vermelho=0, b_branco=0, b_preto=0):

        self.id_pedido = "" 
        self.id_cliente = id_cliente
        self.qtd_b_vermelho = b_vermelho
        self.qtd_b_branco = b_branco
        self.qtd_b_preto = b_preto
        self.fg_ativo = 1

        self.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        self.cursor = self.conn.cursor();

        self.cursor.execute('''
                                INSERT INTO tb_pedido(id_cliente, qtd_bojo_vermelho, qtd_bojo_branco, qtd_bojo_preto, fg_ativo)
                                VALUES 
                                (?, ?, ?, ?, ?)''', (self.id_cliente, self.qtd_b_vermelho, self.qtd_b_branco, self.qtd_b_preto, self.fg_ativo) 
                           )

        self.conn.commit()


    def get_pedido(self):

        self.cursor.execute('''
                                SELECT * 
                                FROM tb_pedido
                                WHERE id_pedido = ?
                            ''', (self.id_pedido,)
                            )

        (self.id_pedido, self.id_cliente, self.qtd_b_vermelho, self.qtd_b_branco, self.qtd_b_preto, self.fg_ativo) = self.cursor.fetchone()
        return (self.id_pedido, self.id_cliente, self.qtd_b_vermelho, self.qtd_b_branco, self.qtd_b_preto, self.fg_ativo) 

    @classmethod
    def get_pedido(cls, id_cliente):

        cls.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        cls.cursor = cls.conn.cursor();

        cls.cursor.execute('''
                                SELECT c.nome, c.sobrenome, p.qtd_bojo_vermelho, p.qtd_bojo_branco, p.qtd_bojo_preto
                                FROM tb_pedido p
                                INNER JOIN tb_cliente c ON( p.id_cliente = c.id_cliente)
                                WHERE p.id_cliente= ?
                            ''', (id_cliente,)
                            )

        
        return cls.cursor.fetchall() 


    @classmethod
    def get_pedidos(cls):

        cls.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        cls.cursor = cls.conn.cursor();

        cls.cursor.execute('''
                                SELECT p.id_pedido, c.nome, c.sobrenome, p.qtd_bojo_vermelho, p.qtd_bojo_branco, p.qtd_bojo_preto 
                                FROM tb_pedido p
                                INNER JOIN tb_cliente c ON(p.id_cliente = c.id_cliente)
                            '''
                            )

        return cls.cursor.fetchall()



    def set_pedido(self, id_cliente, qtd_b_vermelho, qtd_b_branco, qtd_b_preto, fg_ativo):

        self.id_cliente = id_cliente
        self.qtd_b_vermelho = qtd_b_vermelho
        self.qtd_b_branco = qtd_b_branco
        self.qtd_b_preto = qtd_b_preto
        self.fg_ativo = fg_ativo

        self.cursor.execute('''
                                UPDATE tb_pedido
                                set id_cliente = ?,
                                    qtd_bojo_vermelho = ?,
                                    qtd_bojo_branco = ?,
                                    qtd_bojo_preto = ?,
                                    fg_ativo = ?
                                where id_pedido = ?
                            ''', ( self.id_cliente, self.qtd_b_vermelho, self.qtd_b_branco, self.qtd_b_preto, self.fg_ativo, self.id_pedido) 
                           )

        self.conn.commit()


    def soma_qtd_pecas(self):
        return self.qtd_b_vermelho + self.qtd_b_branco + self.qtd_b_preto

    def mostrar_pedido(self):
        print("%s\t%s\t%s\t%s\n" % ('Id Cliente', 'Bojos Vermelhos', 'Bojos Brancos', 'Bojos Pretos'))
        print("%d\t%d\t%d\t%d\n" % (self.id_cliente, self.qtd_b_vermelho, self.qtd_b_branco, self.qtd_b_preto))



if __name__ == '__main__':

    #meu_pedido1 = Pedido(1,10,10,10)
    #meu_pedido1.mostrar_pedido()

    #print(Pedido.get_pedidos())
    print(Pedido.get_pedido(id_cliente=1))






