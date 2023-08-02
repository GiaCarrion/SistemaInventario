import tkinter as tk

class PantallaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de inventario de libros y películas")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        lbl_titulo = tk.Label(self, text="Selecciona una opción:")
        lbl_titulo.pack(pady=10)

        #Cargar imágenes para los botones

        btn_opcion1 = tk.Button(self, text="Opción 1", command=self.abrir_ventana_opcion1)
        btn_opcion1.pack(pady=5)

        btn_opcion2 = tk.Button(self, text="Opción 2", command=self.abrir_ventana_opcion2)
        btn_opcion2.pack(pady=5)

        self.ventanas_secundarias_abiertas = 0  # Variable para contar las ventanas secundarias abiertas

    def abrir_ventana_opcion1(self):
        self.withdraw()  # Oculta la pantalla principal
        ventana_opcion1 = VentanaOpcion1(self)
        self.ventanas_secundarias_abiertas += 1
        ventana_opcion1.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_secundaria)
        ventana_opcion1.mainloop()

    def abrir_ventana_opcion2(self):
        self.withdraw()  # Oculta la pantalla principal
        ventana_opcion2 = VentanaOpcion2(self)
        self.ventanas_secundarias_abiertas += 1
        ventana_opcion2.protocol("WM_DELETE_WINDOW", self.cerrar_ventana_secundaria)
        ventana_opcion2.mainloop()

    def cerrar_ventana_secundaria(self):
        self.ventanas_secundarias_abiertas -= 1
        if self.ventanas_secundarias_abiertas == 0:
            self.destroy()  # Cierra el programa por completo cuando no hay ventanas secundarias abiertas

class VentanaOpcion1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ventana Opción 1")
        self.geometry("300x150")

        self.create_widgets()

    def create_widgets(self):
        lbl_mensaje = tk.Label(self, text="Esta es la ventana de Opción 1")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def regresar_pantalla_principal(self):
        self.master.deiconify()  # Vuelve a mostrar la pantalla principal
        self.destroy()

class VentanaOpcion2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ventana Opción 2")
        self.geometry("300x150")

        self.create_widgets()

    def create_widgets(self):
        lbl_mensaje = tk.Label(self, text="Esta es la ventana de Opción 2")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def regresar_pantalla_principal(self):
        self.master.deiconify()  # Vuelve a mostrar la pantalla principal
        self.destroy()

if __name__ == "__main__":
    app = PantallaPrincipal()
    app.mainloop()
