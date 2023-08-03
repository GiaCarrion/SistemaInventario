import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class PantallaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de inventario de libros y películas")
        self.state('zoomed')  # Maximizar la ventana principal (modo pantalla completa)

        self.create_widgets()

    def create_widgets(self):
        lbl_titulo = tk.Label(self, text="Selecciona una opción:")
        lbl_titulo.pack(pady=10)

        # Frame para contener el ttk.Notebook
        frame_notebook = tk.Frame(self)
        frame_notebook.pack(pady=10)

        # ttk.Notebook para contener las pestañas (ventanas secundarias)
        notebook = ttk.Notebook(frame_notebook)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Pestaña Opción 1
        opcion1_tab = ttk.Frame(notebook)
        notebook.add(opcion1_tab, text="Libros")
        self.create_opcion1_widgets(opcion1_tab)

        # Pestaña Opción 2
        opcion2_tab = ttk.Frame(notebook)
        notebook.add(opcion2_tab, text="Películas")
        self.create_opcion2_widgets(opcion2_tab)

    def create_opcion1_widgets(self, frame):
        lbl_mensaje = tk.Label(frame, text="Esta es la ventana de Opción 1")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(frame, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def create_opcion2_widgets(self, frame):
        lbl_mensaje = tk.Label(frame, text="Esta es la ventana de Opción 2")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(frame, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def regresar_pantalla_principal(self):
        self.deiconify()  # Vuelve a mostrar la pantalla principal

if __name__ == "__main__":
    app = PantallaPrincipal()
    app.mainloop()
