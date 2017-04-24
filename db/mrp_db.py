#!/bin/env python

import sqlite3


conn = sqlite3.connect('mrp-db.sqlite')
cursor = conn.cursor()


#Criando as tabelas

cursor.execute('''
               create table tb_estoque( 
                  id_estoque integer primary key autoincrement, 
                  id_fabrica integer,
                  qtd_tec_verm real,
                  qtd_tec_branco real,
                  qtd_tec_preto real,
                  qtd_espuma real)
               ''')


cursor.execute('''
                 create table tb_cliente(
                    id_cliente integer primary key autoincrement, 
                    nome text,
                    sobrenome text)
               ''')


cursor.execute('''
                create table tb_fabrica(
                    id_fabrica integer primary key,
                    cidade text,
                    estado text)
               ''')

cursor.execute('''
                create table tb_pedido(
                    id_pedido integer primary key autoincrement, 
                    id_cliente integer,
                    qtd_bojo_vermelho integer,
                    qtd_bojo_branco integer,
                    qtd_bojo_preto integer,
                    fg_ativo integer)
                ''')

cursor.execute('''
                insert into tb_cliente(nome,sobrenome)
                values
                (?,?)
                ''', ("Alan", "Turing")
               )

conn.commit()
