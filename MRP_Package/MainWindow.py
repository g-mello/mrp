#!/usr/bin/env python
# -*- coding: latin-1 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sqlite3

import Pedido, Cliente, Dialogs


class MainWindow(Gtk.Window):
    
    def __init__(self):

        Gtk.Window.__init__(self, title="Trabalho MRP")
        self.set_border_width(30)
        self.set_size_request(800,300)

        self.clientes = Cliente.Cliente.get_clientes()

         # Stack - container that shows one item at a time
        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(1000)

        # StackSwitcher - controller for the stack (row of buttons you can click to change items)
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)

        #Grid
        grid = Gtk.Grid()
        self.add(grid)

        #Layout Clientes
        #layout_clientes = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        layout_clientes = Gtk.Grid()
        layout_clientes.set_row_spacing(30)
        #layout_clientes.set_homogeneous(False)


        label_cliente = Gtk.Label()
        label_cliente.set_markup(" <big><b>Clientes</b></big>")
        label_cliente.set_line_wrap(True)

        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        clientes_list_store = Gtk.ListStore(int, str, str)
        for c in self.clientes:
            clientes_list_store.append(list(c))

        # TreeView is the item that is displayed
        clientes_tree_view = Gtk.TreeView(clientes_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Id", "Nome", "Sobrenome"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            clientes_tree_view.append_column(column)


        label_busca_pedido = Gtk.Label()
        label_busca_pedido.set_markup("<big><b> Buscar Pedido do Cliente: </b></big>")

        self.id_cliente = Gtk.Entry()
        self.id_cliente.set_placeholder_text("Id do Cliente")

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)
        self.button_busca_pedido = Gtk.Button(label="Buscar")
        self.button_busca_pedido.connect("clicked", self.buscar_pedido)

        button_box.pack_start(label_busca_pedido, True, True, 0)
        button_box.pack_start(self.id_cliente, True, True, 0)
        button_box.pack_start(self.button_busca_pedido, True, True, 0)


        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        clientes_list_store = Gtk.ListStore(int, str, str)
        for c in self.clientes:
            clientes_list_store.append(list(c))

        # TreeView is the item that is displayed
        clientes_tree_view = Gtk.TreeView(clientes_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Id", "Nome", "Sobrenome"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            clientes_tree_view.append_column(column)


        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        self.pedido_list_store = Gtk.ListStore(str, str, int, int, int)

        # TreeView is the item that is displayed
        self.pedido_tree_view = Gtk.TreeView(self.pedido_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate([ "Nome do Cliente", "Sobrenome do Cliente", "Qtd Bojo Vermelho", "Qtd Bojo Branco", "Qtd Bojo Preto"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            self.pedido_tree_view.append_column(column)




        # Setting Layout Clientes 
        '''
        layout_clientes.pack_start(box_cliente, True, True, 0)
        layout_clientes.pack_start(clientes_tree_view, False, False, 0)
        layout_clientes.pack_start(button_box, True, True, 0)
        layout_clientes.pack_start(box_pedido, True, True, 0)
        '''

        layout_clientes.attach(label_cliente,0,0,1,1) 
        layout_clientes.attach(clientes_tree_view,0,1,1,1) 
        layout_clientes.attach(button_box,0,2,1,1)
        layout_clientes.attach(self.pedido_tree_view,0,3,1,1) 

        main_area.add_titled(layout_clientes, "layout_clientes", "Clientes")



        #Layout Novo Pedido 
        layout_pedidos = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=50)
        layout_pedidos.set_homogeneous(False)
        layout_pedidos.set_border_width(30)
        self.add(layout_pedidos)

        box_cliente = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        label_cliente = Gtk.Label()
        label_cliente.set_markup(" <big><b>Cliente: </b></big>")
        label_cliente.set_line_wrap(True)

        self.nome_cliente = Gtk.Entry()
        self.nome_cliente.set_placeholder_text("Nome do Cliente")

        box_cliente.pack_start(label_cliente, True, True, 0)
        box_cliente.pack_start(self.nome_cliente, True, True, 0)


        #box_bojos = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        grid_bojos = Gtk.Grid()
        grid_bojos.set_border_width(20)

        label_bojo_vermelho = Gtk.Label()
        label_bojo_vermelho.set_markup(" <big><b> Bojo Vermelho: </b></big>")
        label_bojo_vermelho.set_line_wrap(True)

        label_bojo_branco = Gtk.Label()
        label_bojo_branco.set_markup(" <big><b> Bojo Branco: </b></big>")
        label_bojo_branco.set_line_wrap(True)

        label_bojo_preto = Gtk.Label()
        label_bojo_preto.set_markup(" <big><b> Bojo Preto: </b></big>")
        label_bojo_preto.set_line_wrap(True)

        self.qtd_bojo_vermelho = Gtk.Entry()
        self.qtd_bojo_vermelho.set_placeholder_text("Qtd de Peças")

        self.qtd_bojo_branco= Gtk.Entry()
        self.qtd_bojo_branco.set_placeholder_text("Qtd de Peças")

        self.qtd_bojo_preto = Gtk.Entry()
        self.qtd_bojo_preto.set_placeholder_text("Qtd de Peças")

        grid_bojos.attach(label_bojo_vermelho,0,0,1,1)
        grid_bojos.attach(self.qtd_bojo_vermelho,1,0,1,1)
        grid_bojos.attach(label_bojo_branco,0,1,1,1)
        grid_bojos.attach(self.qtd_bojo_branco,1,1,1,1)
        grid_bojos.attach(label_bojo_preto,0,2,1,1)
        grid_bojos.attach(self.qtd_bojo_preto,1,2,1,1)


        box_salvar_cancelar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=30)

        button_add = Gtk.Button(label="Add")
        button_add.connect("clicked", self.add_pedido)

        button_cancelar = Gtk.Button(label="Cancelar")
        button_cancelar.connect("clicked", self.cancelar_pedido)

        box_salvar_cancelar.pack_start(button_add, True, True, 0)
        box_salvar_cancelar.pack_start(button_cancelar, True, True, 0)


        layout_pedidos.pack_start(box_cliente, True, True, 0)
        layout_pedidos.pack_start(grid_bojos, True, True, 0)
        layout_pedidos.pack_start(box_salvar_cancelar, True, True, 0)

        main_area.add_titled(layout_pedidos, "layout_clientes", "Add Pedido")

        #Layout Producão
        layout_producao = Gtk.Grid()
        layout_producao.set_border_width(30)
        layout_producao.set_row_spacing(30)

        label_pedidos = Gtk.Label()
        label_pedidos.set_markup(" <big><b> Pedidos Solicitados: </b></big>")
        label_pedidos.set_line_wrap(True)

        pedidos_list_store = Gtk.ListStore(int, str, str, int, int, int)
        for p in Pedido.Pedido.get_pedidos():
            pedidos_list_store.append(p)

        # TreeView is the item that is displayed
        pedidos_tree_view = Gtk.TreeView(pedidos_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Id", "Nome", "Sobrenome", "Qtd Bojo Vermelho", "Qtd Bojo Branco", "Qtd Bojo Preto"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            pedidos_tree_view.append_column(column)


        label_pedidos_produzidos = Gtk.Label()
        label_pedidos_produzidos.set_markup(" <big><b> Pedidos Produzidos: </b></big>")
        label_pedidos_produzidos.set_line_wrap(True)

        pedidos_produzidos_list_store = Gtk.ListStore(int, str, str, int, int, int)
        for p in Pedido.Pedido.get_pedidos():
            pedidos_produzidos_list_store.append(p)

        # TreeView is the item that is displayed
        pedidos_produzidos_tree_view = Gtk.TreeView(pedidos_produzidos_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Id", "Nome", "Sobrenome", "Qtd Bojo Vermelho", "Qtd Bojo Branco", "Qtd Bojo Preto"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            pedidos_produzidos_tree_view.append_column(column)

        label_estoque = Gtk.Label()
        label_estoque.set_markup(" <big><b> Meu Estoque: </b></big>")
        label_estoque.set_line_wrap(True)

        estoque_list_store = Gtk.ListStore(int, str, str, int, int, int)
        for p in Pedido.Pedido.get_pedidos():
            estoque_list_store.append(p)

        # TreeView is the item that is displayed
        estoque_tree_view = Gtk.TreeView(estoque_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Id", "Nome", "Sobrenome", "Qtd Bojo Vermelho", "Qtd Bojo Branco", "Qtd Bojo Preto"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            estoque_tree_view.append_column(column)


        layout_producao.attach(label_pedidos, 0,0,1,1)
        layout_producao.attach(pedidos_tree_view, 0,1,1,1)
        layout_producao.attach(label_pedidos_produzidos, 0,2,1,1)
        layout_producao.attach(pedidos_produzidos_tree_view, 0,3,1,1)
        layout_producao.attach(label_estoque, 0,4,1,1)
        layout_producao.attach(estoque_tree_view, 0,5,1,1)

        main_area.add_titled(layout_producao, "layout_producao", "Produção")



        grid.attach(stack_switcher, 0, 0, 1, 1)
        grid.attach(main_area, 0, 2, 1, 1)

    def buscar_pedido(self, widget):
        
        id_cliente = self.id_cliente.get_text()
        info = Pedido.Pedido.get_pedido(id_cliente)
        for p in info:
            self.pedido_list_store.append(p)
        

    def add_pedido(self, widget):
        
        n = self.nome_cliente.get_text().split()

        id_cliente = Cliente.Cliente.get_id_cliente(n[0],n[1])
        qtd_b_vermelho = int(self.qtd_bojo_vermelho.get_text())
        qtd_b_branco = int(self.qtd_bojo_branco.get_text())
        qtd_b_preto = int(self.qtd_bojo_preto.get_text())

        p = Pedido.Pedido(10, id_cliente, qtd_b_vermelho, qtd_b_branco, qtd_b_preto)

        del(p)


    def cancelar_pedido(self, widget):
        self.nome_cliente.set_text(" ")
        self.qtd_bojo_vermelho.set_text(" ")
        self.qtd_bojo_branco.set_text(" ")
        self.qtd_bojo_preto.set_text(" ")






if __name__ == '__main__':
    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()
