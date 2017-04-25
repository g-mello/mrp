#!/bin/env python

'''
    Author: Guilherme Mello Oliveira    RA: 18120
    Author: Caio Silva Poli             RA: 18787
'''


from MRP_Package.Fabrica import Fabrica 
from MRP_Package.Pedido import Pedido 
from MRP_Package.Cliente import Cliente
from MRP_Package.MainWindow import MainWindow

from MRP_Package.MainWindow import MainWindow

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

if __name__ == '__main__':

    window = MainWindow()
    window.connect("delete-event", Gtk.main_quit)
    window.show_all()
    Gtk.main()


