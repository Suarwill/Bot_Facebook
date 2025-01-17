import importlib as ilib
import subprocess as sub
def libSetup(lib):
    # Funcion para instalar automaticamente librerias no existentes
    try:ilib.import_module(lib)
    except ImportError:sub.check_call(['pip', 'install', lib])

libSetup('tkinter')
from tkinter import *
from tkinter import messagebox

def start():
    print("iniciamos bien")

def ventanaLikear():
    # Crear nueva ventana
    nueva_ventana = Toplevel(ventana)
    nueva_ventana.title("Dar Like")

    # Recuadro para texto
    texto_label = Label(nueva_ventana, text="Texto:")
    texto_label.grid(row=0, column=0)
    texto_entry = Entry(nueva_ventana)
    texto_entry.grid(row=0, column=1)

    # Botón "Empezar"
    empezar_button = Button(nueva_ventana, text="Empezar", command=lambda: likear(texto_entry.get()))
    empezar_button.grid(row=1, column=0, columnspan=2)


def likear(texto):
    print(f"Texto ingresado: {texto}")
    # Aquí iría la lógica para dar like con el texto ingresado
    # ...

def comentario():
    # funcion de comentar
    return print("comentarios publicados")

def publicar():
    # funcion de comentar
    return print("publicaciones realizadas")

def compartir():
    # funcion de comentar
    return print("compartido")

# Inicio de GUI
ventana = Tk()
ventana.title("Bot de Facebook")

# Configuración de tamaño y posición de la ventana
width, heigth = 300, 150
puntoMedioAnchura , puntoMedioAlto = int((ventana.winfo_screenwidth()-width)/2), int((ventana.winfo_screenheight()-heigth)/2)
ventana.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

# Variables de posicionamiento
posRowDiferencias, posColDiferencias  = 1 , 3
posRowLimp , posColLimp = 1 , 1
space, colcentral = 2 , 2

#Etiquetas
#mensaje = Label(ventana, text="Uso bajo Licencia").grid(row=5, column=colcentral)
separador_0 = Label(ventana, text=" ").grid(row=0, column=colcentral)
separador_2 = Label(ventana, text=" ").grid(row=2, column=colcentral)

#Botones
botonPublicar = Button(ventana, text="Publicar", command=start)
botonPublicar.grid(row=1, column=1, sticky="news")
botonComentar = Button(ventana, text="Comentar", command=start)
botonComentar.grid(row=3, column=1, sticky="news")

botonLikear = Button(ventana, text="Dar Like", command=start)
botonLikear.grid(row=1, column=3, sticky="news")
botonCompartir = Button(ventana, text="Compartir", command=start)
botonCompartir.grid(row=3, column=3, sticky="news")

# Expandir columnas hasta el borde (laterales)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)
ventana.grid_columnconfigure(4, weight=1)

# Bucle
ventana.mainloop()