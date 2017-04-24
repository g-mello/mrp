#!/usr/bin/env python

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 
'''

from __future__ import print_function 
import sqlite3


class Estoque_MP(object):

    def __init__(self, id_estoque, tec_vermelho=0, tec_branco=0, tec_preto=0, espuma=0.0):
        self.id_estoque = id_estoque
        self.qtd_tec_vermelho = tec_vermelho
        self.qtd_tec_branco = tec_branco
        self.qtd_tec_preto = tec_preto
        self.qtd_espuma = espuma
        self.conn = sqlite3.connect("/home/gmello/Projects/python/trabalho_ely_mrp/mrp/db/mrp-db.sqlite")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                                INSERT INTO tb_estoque
                                VALUES 
                                (?, ?, ?, ?, ?)''', (self.id_estoque, self.qtd_tec_vermelho, self.qtd_tec_branco, self.qtd_tec_preto, self.qtd_espuma) 
                           )

        self.conn.commit()


    def get_estoque(self):
          self.cursor.execute('''
                                SELECT * 
                                FROM tb_estoque
                                WHERE id_estoque = ?
                            ''', (self.id_estoque,)
                            )

          (self.id_estoque, self.tec_vermelho, self.tec_branco, self.tec_preto, self.espuma) = self.cursor.fetchone()
          return (self.id_estoque, self.tec_vermelho, self.tec_branco, self.tec_preto, self.espuma) 


    def set_estoque(self, tec_verm, tec_branco, tec_preto, espuma):

        self.qtd_tec_vermelho = tec_verm
        self.qtd_tec_branco = tec_branco
        self.qtd_tec_preto = tec_preto
        self.qtd_espuma = espuma 

        self.cursor.execute('''
                                UPDATE tb_estoque
                                SET qtd_tec_verm = ?,
                                    qtd_tec_branco = ?,
                                    qtd_tec_preto = ?,
                                    qtd_espuma = ?
                                WHERE id_estoque = ?
                            ''', (tec_verm, tec_branco, tec_preto, espuma, self.id_estoque)
                            )
        self.conn.commit()



    def mostrar_estoque(self):

        print("%-30s\t%-30s\t%-30s\t%-30s\n" % ("Tecido Vermelho(kg)", "Tecido Branco(kg)", "Tecido Preto(kg)", "Espuma(metros)"))
        print("%-30.2f\t%-30.2f\t%-30.2f\t%-30.2f\n" % (self.qtd_tec_vermelho, self.qtd_tec_branco, self.qtd_tec_preto, self.qtd_espuma))

    def mostrar_total(self):
        print("Total Tecido em estoque: %d m\n" %(self.qtd_tec_vermelho + self.qtd_tec_branco + self.qtd_tec_preto))
        print("Total Espuma em estoque: %d kg\n" %(self.qtd_espuma))


if __name__ == '__main__':

    meu_estoque = Estoque_MP(10, 10, 10, 10, 10)
    meu_estoque.mostrar_estoque()
    meu_estoque.set_estoque(20,20,20,20)
    meu_estoque.mostrar_estoque()
    print(meu_estoque.get_estoque())




