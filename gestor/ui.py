# gestor/ui.py

import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import gestor.database as db

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestor de Clientes")
        self.geometry("500x400")
        self.build()

    def build(self):
        # Crear Treeview
        self.treeview = ttk.Treeview(self, columns=("DNI", "Nombre", "Apellido"), show="headings")
        self.treeview.heading("DNI", text="DNI")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear frame de botones
        frame = tk.Frame(self)
        frame.pack(pady=10)

        btn_add = tk.Button(frame, text="Añadir Cliente", command=self.añadir_cliente)
        btn_add.grid(row=0, column=0, padx=5)

        btn_edit = tk.Button(frame, text="Modificar Cliente", command=self.modificar_cliente)
        btn_edit.grid(row=0, column=1, padx=5)

        btn_delete = tk.Button(frame, text="Borrar Cliente", command=self.borrar_cliente)
        btn_delete.grid(row=0, column=2, padx=5)

        btn_exit = tk.Button(frame, text="Salir", command=self.destroy)
        btn_exit.grid(row=0, column=3, padx=5)

        # Cargar datos
        self.cargar_datos()

    def cargar_datos(self):
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        for cliente in db.Clientes.lista:
            self.treeview.insert("", tk.END, values=(cliente.dni, cliente.nombre, cliente.apellido))

    def añadir_cliente(self):
        dni = simpledialog.askstring("DNI", "Introduce el DNI (2 números y 1 letra)").upper()
        if not dni or not dni.isalnum() or len(dni) != 3:
            messagebox.showerror("Error", "DNI inválido.")
            return
        if db.Clientes.buscar(dni):
            messagebox.showerror("Error", "Ese DNI ya existe.")
            return
        nombre = simpledialog.askstring("Nombre", "Introduce el nombre")
        apellido = simpledialog.askstring("Apellido", "Introduce el apellido")
        if nombre and apellido:
            db.Clientes.crear(dni, nombre, apellido)
            self.cargar_datos()

    def modificar_cliente(self):
        seleccionado = self.treeview.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un cliente primero.")
            return
        cliente_actual = self.treeview.item(seleccionado)["values"]
        dni = cliente_actual[0]
        nombre_nuevo = simpledialog.askstring("Nuevo nombre", "Introduce el nuevo nombre", initialvalue=cliente_actual[1])
        apellido_nuevo = simpledialog.askstring("Nuevo apellido", "Introduce el nuevo apellido", initialvalue=cliente_actual[2])
        if nombre_nuevo and apellido_nuevo:
            db.Clientes.modificar(dni, nombre_nuevo, apellido_nuevo)
            self.cargar_datos()

    def borrar_cliente(self):
        seleccionado = self.treeview.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Selecciona un cliente primero.")
            return
        cliente_actual = self.treeview.item(seleccionado)["values"]
        confirmacion = messagebox.askyesno("Confirmar", f"¿Seguro que quieres borrar a {cliente_actual[1]} {cliente_actual[2]}?")
        if confirmacion:
            db.Clientes.borrar(cliente_actual[0])
            self.cargar_datos()