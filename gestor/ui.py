

# gestor/ui.py

import tkinter as tk
from tkinter import ttk
import gestor.database as db

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.geometry("500x300")
        self.build()

    def build(self):
        # Crear Treeview
        self.treeview = ttk.Treeview(self, columns=("DNI", "Nombre", "Apellido"), show="headings")
        self.treeview.heading("DNI", text="DNI")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Cargar datos
        self.cargar_datos()

    def cargar_datos(self):
        for cliente in db.Clientes.lista:
            self.treeview.insert("", tk.END, values=(cliente.dni, cliente.nombre, cliente.apellido))