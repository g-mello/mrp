#!/bin/env python

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 18xxx
'''


from MRP_Package.Fabrica import Fabrica 
from MRP_Package.Pedido import Pedido 

if __name__ == '__main__':

    #Cria uma instacia da Fabrica e inicializa seu estoque
    minha_fabrica = Fabrica()
    minha_fabrica.set_estoque(40,60,50,600)

    print("\nEstoque Inicial\n")
    minha_fabrica.estoque.mostrar_estoque()

    # Cria 3 instancias de Pedido 
    meu_pedido_1 = Pedido("Alan Turing", 200, 200, 0)
    meu_pedido_2 = Pedido("Bill Gates", 200, 200, 300)
    meu_pedido_3 = Pedido("Steve Jobs", 0, 650, 450)

    #Adiciona os Pedidos na produção
    minha_fabrica.add_pedido(*meu_pedido_1.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_2.get_pedido())
    minha_fabrica.add_pedido(*meu_pedido_3.get_pedido())

    #Coloca os pedidos em produção de acordo com a quantidade disponivel 
    #em estoqu, mostrando as quantidade produzidas
    minha_fabrica.produzir()

    print("\nEstoque Restante\n")
    minha_fabrica.estoque.mostrar_estoque()


