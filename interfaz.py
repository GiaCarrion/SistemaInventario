import tkinter as tk
from PIL import Image, ImageTk

class PantallaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de inventario de libros y películas")
        
        # Maximizar la ventana principal (modo pantalla completa)
        self.state('zoomed')

        self.create_widgets()

    def create_widgets(self):
        lbl_titulo = tk.Label(self, text="Selecciona una opción:")
        lbl_titulo.pack(pady=10)

        # Frame para contener los botones
        frame_botones = tk.Frame(self)
        frame_botones.pack(side=tk.TOP, pady=50)

        # Cargar imágenes con PIL y ImageTk
        imagen_libro = Image.open(r"C:\Users\giane\OneDrive\Escritorio\SistemaInventario\image\libro.png")
        imagen_libro = imagen_libro.resize((300, 300))  # Redimensionar la imagen
        imagen_libro = ImageTk.PhotoImage(imagen_libro)

        imagen_pelicula = Image.open(r"C:\Users\giane\OneDrive\Escritorio\SistemaInventario\image\pelicula.png")
        imagen_pelicula = imagen_pelicula.resize((300, 300))  # Redimensionar la imagen
        imagen_pelicula = ImageTk.PhotoImage(imagen_pelicula)

        # Botón Opción 1
        btn_opcion1 = tk.Button(frame_botones, image=imagen_libro, compound=tk.TOP, text="Libros", command=self.abrir_ventana_opcion1)
        btn_opcion1.image = imagen_libro  # Asignar imagen al botón
        btn_opcion1.pack(side=tk.LEFT, padx=50, pady=50, anchor=tk.CENTER)

        # Botón Opción 2
        btn_opcion2 = tk.Button(frame_botones, image=imagen_pelicula, compound=tk.TOP, text="Películas", command=self.abrir_ventana_opcion2)
        btn_opcion2.image = imagen_pelicula  # Asignar imagen al botón
        btn_opcion2.pack(side=tk.RIGHT, padx=50, pady=50, anchor=tk.CENTER)

        self.ventanas_secundarias_abiertas = 0

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
        self.state('zoomed')

        self.create_widgets()

    def create_widgets(self):
        lbl_mensaje = tk.Label(self, text="Esta es la ventana de Opción 1")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def regresar_pantalla_principal(self):
        self.master.state('zoomed')
        self.destroy()

class VentanaOpcion2(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Ventana Opción 2")
        self.state('zoomed')

        self.create_widgets()

    def create_widgets(self):
        lbl_mensaje = tk.Label(self, text="Esta es la ventana de Opción 2")
        lbl_mensaje.pack(pady=10)

        btn_regresar = tk.Button(self, text="Regresar", command=self.regresar_pantalla_principal)
        btn_regresar.pack(pady=5)

    def regresar_pantalla_principal(self):
        self.master.state('zoomed')
        self.destroy()

if __name__ == "__main__":
    app = PantallaPrincipal()
    app.mainloop()