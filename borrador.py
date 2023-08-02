import tkinter as tk
from tkinter import messagebox
from conexion import Registro_funciones

class InterfazRegistro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aplicación de Registro")
        self.geometry("400x300")

        self.registro = Registro_funciones()

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas
        lbl_codigo = tk.Label(self, text="Código:")
        lbl_codigo.grid(row=0, column=0, padx=10, pady=5)
        lbl_titulo = tk.Label(self, text="Título:")
        lbl_titulo.grid(row=1, column=0, padx=10, pady=5)
        lbl_autor = tk.Label(self, text="Autor:")
        lbl_autor.grid(row=2, column=0, padx=10, pady=5)
        lbl_editorial = tk.Label(self, text="Editorial:")
        lbl_editorial.grid(row=3, column=0, padx=10, pady=5)
        lbl_anio = tk.Label(self, text="Año:")
        lbl_anio.grid(row=4, column=0, padx=10, pady=5)
        lbl_ubicacion = tk.Label(self, text="Ubicación:")
        lbl_ubicacion.grid(row=5, column=0, padx=10, pady=5)

        # Cuadros de texto
        self.txt_codigo = tk.Entry(self)
        self.txt_codigo.grid(row=0, column=1, padx=10, pady=5)
        self.txt_titulo = tk.Entry(self)
        self.txt_titulo.grid(row=1, column=1, padx=10, pady=5)
        self.txt_autor = tk.Entry(self)
        self.txt_autor.grid(row=2, column=1, padx=10, pady=5)
        self.txt_editorial = tk.Entry(self)
        self.txt_editorial.grid(row=3, column=1, padx=10, pady=5)
        self.txt_anio = tk.Entry(self)
        self.txt_anio.grid(row=4, column=1, padx=10, pady=5)
        self.txt_ubicacion = tk.Entry(self)
        self.txt_ubicacion.grid(row=5, column=1, padx=10, pady=5)

        # Botones
        btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_registro)
        btn_agregar.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        btn_mostrar = tk.Button(self, text="Mostrar", command=self.mostrar_registros)
        btn_mostrar.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        btn_buscar = tk.Button(self, text="Buscar", command=self.buscar_registro)
        btn_buscar.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
        btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_registro)
        btn_eliminar.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

    def agregar_registro(self):
        codigo = self.txt_codigo.get()
        titulo = self.txt_titulo.get()
        autor = self.txt_autor.get()
        editorial = self.txt_editorial.get()
        año = self.txt_anio.get()
        ubicacion = self.txt_ubicacion.get()

        # Llama a la función agregar del objeto Registro_funciones
        self.registro.agregar(codigo, titulo, autor, editorial, año, ubicacion)

        messagebox.showinfo("Éxito", "Registro agregado correctamente.")

    def mostrar_registros(self):
        registros = self.registro.mostrar()
        if registros:
            for registro in registros:
                print(registro)
        else:
            messagebox.showinfo("No hay registros", "No hay registros en la base de datos.")

    def buscar_registro(self):
        titulo = self.txt_titulo.get()
        resultado = self.registro.buscar(titulo)
        if resultado:
            print(resultado)
        else:
            messagebox.showinfo("No encontrado", f"No se encontró ningún registro con el título '{titulo}'.")

    def eliminar_registro(self):
        titulo = self.txt_titulo.get()
        self.registro.eliminar(titulo)
        messagebox.showinfo("Éxito", f"Registro con el título '{titulo}' eliminado correctamente.")

if __name__ == "__main__":
    app = InterfazRegistro()
    app.mainloop()

