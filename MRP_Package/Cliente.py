#!/usr/bin/env python

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
import sqlite3

class Cliente(object):

    def __init__(self, nome="default", sobrenome="default"):

        self.id_cliente = "" 
        self.nome = nome
        self.sobrenome = sobrenome

        self.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        self.cursor = self.conn.cursor();

        self.cursor.execute('''
                                INSERT INTO tb_cliente( nome, sobrenome)
                                VALUES 
                                (?, ?)''', (self.nome, self.sobrenome) 
                           )

        self.conn.commit()


    def get_cliente(self):

        self.cursor.execute('''
                                SELECT * 
                                FROM tb_cliente
                                WHERE id_cliente= ?
                            ''', (self.id_cliente,)
                            )

        (self.id_cliente, self.nome, self.sobrenome) = self.cursor.fetchone()
        return (self.id_cliente, self.nome, self.sobrenome) 

    @classmethod
    def get_clientes(cls):

        cls.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        cls.cursor = cls.conn.cursor();
        
        cls.cursor.execute('''
                                SELECT * 
                                FROM tb_cliente
                            '''
                            )

        
        return cls.cursor.fetchall()

    @classmethod
    def get_id_cliente(cls, nome, sobrenome):

        cls.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        cls.cursor = cls.conn.cursor();
        
        cls.cursor.execute('''
                                SELECT id_cliente 
                                FROM tb_cliente
                                WHERE nome = ?
                                and sobrenome = ?
                            ''', (nome, sobrenome)
                            )

        
        return cls.cursor.fetchone()[0]




    def set_cliente(self, nome, sobrenome, id_cliente):

        self.id_cliente = id_cliente
        self.nome = nome
        self.sobrenome = sobrenome

        self.cursor.execute('''
                                UPDATE tb_cliente
                                SET nome = ?,
                                    sobrenome = ?
                                WHERE id_cliente = ?
                            ''', ( self.nome, self.sobrenome, self.id_cliente) 
                           )

        self.conn.commit()


    def mostrar_cliente(self):
        print("%s\t%s\n" % ('Nome', 'Sobrenome'))
        print("%s\t%s\n" % (self.nome, self.sobrenome))



if __name__ == '__main__':

    cliente = Cliente("Alan", "Turing")
    cliente.mostrar_cliente()

    #print(Cliente.get_clientes())
    #print(Cliente.get_id_cliente("Alan", "Turing"))





