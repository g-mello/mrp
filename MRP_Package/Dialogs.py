#!/usr/bin/env python
# -*- coding: latin-1 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import Pedido 

class PedidoDialog(Gtk.Dialog, Gtk.Window):

    def __init__(self, parent, id_cliente):

        # self, title, parent, flags (MODAL prevent interaction with main window until dialog returns), buttons
        Gtk.Dialog.__init__(self, "Pedido", parent, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))
        
        self.set_border_width(30)
        self.set_default_size(800, 300)
        box = self.get_content_area()

        layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        layout.set_homogeneous(False)
        layout.set_border_width(30)

        box_cliente = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        box.set_homogeneous(False)

        label_cliente = Gtk.Label()
        label_cliente.set_markup(" <big><b>CLiente: </b></big>")
        label_cliente.set_line_wrap(True)

        label_nome = Gtk.Label()
        label_nome.set_markup(" <big><b>Nome do Cliente Aqui </b></big>")
        label_nome.set_line_wrap(True)

        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        pedido_list_store = Gtk.ListStore(int, int, int, int, int)
        #pedido_list_store.append(["Bojo", "Vermelho", 100])
        for p in Pedido.Pedido.get_pedido(id_cliente): 
            pedido_list_store.append(p)

        # TreeView is the item that is displayed
        pedido_tree_view = Gtk.TreeView(pedido_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["iD", "ID", "Qtd Bojo Vermelho", "Qtd Bojo Branco", "Qtd Bojo Preto"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            pedido_tree_view.append_column(column)

        box_cliente.pack_start(label_cliente, True, True, 0)
        box_cliente.pack_start(label_nome, True, True, 0)


        box_materia_prima = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        box_materia_prima.set_homogeneous(False)

        label_materia_prima = Gtk.Label()
        label_materia_prima.set_markup(" <big><b>Gasto de Materia Prima</b></big>")
        label_materia_prima.set_line_wrap(True)

        # Convert data to ListStore (lists that TreeViews can display) and specify data types
        materia_prima_list_store = Gtk.ListStore(float, float, float, float)
        materia_prima_list_store.append([10.0, 10.0, 10.0, 10.0])

        # TreeView is the item that is displayed
        materia_prima_tree_view = Gtk.TreeView(materia_prima_list_store)

        # Enumerate to add counter (i) to loop
        for i, col_title in enumerate(["Tecido Vermelho", "Tecido Branco", "Tecido Preto", "Espuma"]):

            # Render means draw or display the data (just display as normal text)
            renderer = Gtk.CellRendererText()
            renderer.set_padding(50,20)

            # Create columns (text is column number)
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # Add columns to TreeView
            materia_prima_tree_view.append_column(column)

        box_materia_prima.pack_start(label_materia_prima, True, True, 0)

        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        layout.pack_start(box_cliente, True, True, 0)
        layout.pack_start(pedido_tree_view, False, False, 0)
        layout.pack_start(hseparator, True, True, 0)
        layout.pack_start(box_materia_prima, True, True, 0)
        layout.pack_start(materia_prima_tree_view, False, False, 0)


        box.add(layout)
        self.show_all()






class AddPedidoDialog(Gtk.Dialog):

    def __init__(self, parent):

        # self, title, parent, flags (MODAL prevent interaction with main window until dialog returns), buttons
        Gtk.Dialog.__init__(self, "Pedido Adicionado", parent, Gtk.DialogFlags.MODAL,
                            (Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(200, 100)
        self.set_border_width(10)

        # Content area (area above buttons)
        area = self.get_content_area()
        area.add(Gtk.Label("Pedido Adicionado Com Sucesso"))
        self.show_all()


