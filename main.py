import importlib as ilib
import subprocess as sub

def libSetup(lib):
    try:
        ilib.import_module(lib)
    except ImportError:
        sub.check_call(['pip', 'install', lib])

libSetup('tkinter')
from tkinter import *
from tkinter import messagebox

def accion(tipo, texto):
    print(f"{tipo}: {texto}")
    # Aquí iría la lógica para interactuar con Facebook según el tipo de acción
    # ...


def crear_ventana(titulo, accion_tipo):
    ventana_nueva = Toplevel(ventana)
    ventana_nueva.title(titulo)

    # Geometría (centrar la ventana)
    width, height = 200, 150
    x = (ventana_nueva.winfo_screenwidth() - width) // 2
    y = (ventana_nueva.winfo_screenheight() - height) // 2
    ventana_nueva.geometry(f"{width}x{height}+{x}+{y}")

    # Recuadro para texto
    Label(ventana_nueva, text="Texto:").grid(row=0, column=0)
    texto_entry = Entry(ventana_nueva)
    texto_entry.grid(row=0, column=1)

    # Botón "Empezar"
    Button(ventana_nueva, text="Empezar", command=lambda: accion(accion_tipo, texto_entry.get())).grid(row=1, column=0, columnspan=2)


# Inicio de GUI
ventana = Tk()
ventana.title("Bot de Facebook")

# Geometría (centrar la ventana principal)
width, height = 300, 150
x = (ventana.winfo_screenwidth() - width) // 2
y = (ventana.winfo_screenheight() - height) // 2
ventana.geometry(f"{width}x{height}+{x}+{y}")


# Botones
acciones = {
    "Publicar": "publicar",
    "Comentar": "comentar",
    "Dar Like": "likear",
    "Compartir": "compartir",
}

for i, (texto_boton, accion_tipo) in enumerate(acciones.items()):
    row = i % 2 + 1  # Alternar filas 1 y 3
    col = i // 2 * 2 + 1 # Alternar columnas 1 y 3
    Button(ventana, text=texto_boton, command=lambda tipo=accion_tipo: crear_ventana(texto_boton, tipo)).grid(row=row, column=col, sticky="news")


# Expandir columnas hasta el borde (laterales y centrales)
for i in range(5):
    ventana.grid_columnconfigure(i, weight=1)

# Bucle
ventana.mainloop()
