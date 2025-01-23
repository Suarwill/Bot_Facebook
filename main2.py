class Ventana:
    def __init__(self, titulo, width, height):
        self.ventana = Tk()
        self.ventana.title(titulo)
        self.ventana.geometry(f"{width}x{height}+{int((self.ventana.winfo_screenwidth()-width)/2)}+{int((self.ventana.winfo_screenheight()-height)/2)}")

    def crearBoton(self, texto, comando, fila, columna, **kwargs):
        Button(self.ventana, text=texto, command=comando, **kwargs).grid(row=fila, column=columna, sticky="news")

    def crearEtiqueta(self, texto, fila, columna, **kwargs):
        Label(self.ventana, text=texto, **kwargs).grid(row=fila, column=columna, padx=5, pady=5)

    def crearEntradaTexto(self, fila, columna, width, height, **kwargs):
        Text(self.ventana, width=width, height=height, **kwargs).grid(row=fila, column=columna, padx=5, pady=5)

    def expandirColumnas(self, num_columnas):
        for x in range(num_columnas):
            self.ventana.grid_columnconfigure(x, weight=1)

    def iniciar(self):
        self.ventana.mainloop()

class VentanaPrincipal(Ventana):
    def __init__(self):
        super().__init__("Principal", 500, 400)

        self.crearEtiqueta(" ", 0, 0)
        self.crearBoton("Publicar", lambda: VentanaSecundaria(self.ventana), 1, 1, background="lightblue")
        self.expandirColumnas(5)

class VentanaSecundaria(Ventana):
    def __init__(self, ventana_padre):
        super().__init__("Secundaria", 700, 300)

        self.crearEtiqueta("Archivo:", 0, 0)
        self.crearEntradaTexto(0, 1, 30, 1)


if __name__ == "__main__":
    import importlib as ilib
    import subprocess as sub
    def libSetup(lib):
        # Funcion para instalar automaticamente librerias no existentes
        try:ilib.import_module(lib)
        except ImportError:sub.check_call(['pip', 'install', lib])
        return
        
    libSetup('tkinter')
    from tkinter import *
    libSetup('warnings')
    import warnings

    ventanaPrincipal = VentanaPrincipal()
    ventanaPrincipal.iniciar()