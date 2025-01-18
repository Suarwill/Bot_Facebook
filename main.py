import importlib as ilib
import subprocess as sub
def libSetup(lib):
    # Funcion para instalar automaticamente librerias no existentes
    try:ilib.import_module(lib)
    except ImportError:sub.check_call(['pip', 'install', lib])

import os, time, csv

libSetup('tkinter')
from tkinter import *
from tkinter import messagebox

libSetup('warnings')
import warnings

libSetup('python-dotenv')
from dotenv import load_dotenv

libSetup('selenium')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def ventanaPublicar():
    ventanaPublicar = Toplevel(ventana)
    ventanaPublicar.title("Dar Like")

    # Geometria
    width, heigth = 200, 200
    puntoMedioAnchura , puntoMedioAlto = int((ventanaPublicar.winfo_screenwidth()-width)/4), int((ventanaPublicar.winfo_screenheight()-heigth)/4)
    ventanaPublicar.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

    # Recuadro para texto
    texto_label = Label(ventanaPublicar, text="Texto:")
    texto_label.grid(row=0, column=0)
    texto_entry = Entry(ventanaPublicar)
    texto_entry.grid(row=0, column=1)

    # Botón "Empezar"
    empezar_button = Button(ventanaPublicar, text="Empezar", command=lambda: likear(texto_entry.get()))
    empezar_button.grid(row=1, column=0, columnspan=2)

def ventanaLikear():
    ventanaLikear = Toplevel(ventana)
    ventanaLikear.title("Dar Like")

    # Geometria
    width, heigth = 200, 150
    puntoMedioAnchura , puntoMedioAlto = int((ventanaLikear.winfo_screenwidth()-width)/4), int((ventanaLikear.winfo_screenheight()-heigth)/4)
    ventanaLikear.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

    # Recuadro para texto
    texto_label = Label(ventanaLikear, text="Texto:")
    texto_label.grid(row=0, column=0)
    texto_entry = Entry(ventanaLikear)
    texto_entry.grid(row=0, column=1)

    # Botón "Empezar"
    empezar_button = Button(ventanaLikear, text="Empezar", command=lambda: likear(texto_entry.get()))
    empezar_button.grid(row=1, column=0, columnspan=2)

def ventanaComentar():
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

def ventanaCompartir():
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
    return print(texto)

def comentario():
    # funcion de comentar
    return print("comentarios publicados")

def publicar():
    driver = webdriver.Chrome()
    AccesoWEB(driver)
    time.sleep(1)

    web = "https://www.facebook.com/groups/"
    objetivos = docCSV('./Objetivos/Grupos.csv')
    post = "texto"

    for x in objetivos:
        driver.get(web+x)
        try:
            botonPost  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Escribe algo...')]/ancestor::div[contains(@role,'textbox')]")))
            selectBotonPost = Select(botonPost)
            selectBotonPost.click()
            time.sleep(2)
            cajaPost  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Crea una publicación pública...')]/ancestor::div[contains(@role,'textbox')]")))
            selectCajaPost = Select(cajaPost)
            selectCajaPost.send_keys(post)
        except (NoSuchElementException, TimeoutException) as e:
            print(e)
        print("publicacion realizada en: ",x)

def compartir():
    # funcion de comentar
    # ajustando
    return print("compartido")

def AccesoWEB(driver):
    web = "https://www.facebook.com"
    login = "/login/"
    userF = os.getenv("FACEBOOK_USERNAME")
    passF = os.getenv("FACEBOOK_PASSWORD")

    driver.get(web+login)
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email_container")))
    username_field.send_keys(userF)
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    password_field.send_keys(passF)
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "loginbutton")))
    login_button.click()
    return

def docCSV(documento):
    with open(documento, 'r') as csvfile:
        reader = csv.reader(csvfile)
        listado = {row[0]: row[0] for row in reader}
    return listado

# Inicio de GUI
ventana = Tk()
ventana.title("Bot de Facebook")

# Configuración de tamaño y posición de la ventana
width, heigth = 300, 150
puntoMedioAnchura , puntoMedioAlto = int((ventana.winfo_screenwidth()-width)/2), int((ventana.winfo_screenheight()-heigth)/2)
ventana.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()

# Variables de posicionamiento
posRowDiferencias, posColDiferencias  = 1 , 3
posRowLimp , posColLimp = 1 , 1
space, colcentral = 2 , 2

#Etiquetas
#mensaje = Label(ventana, text="Uso bajo Licencia").grid(row=5, column=colcentral)
separador_0 = Label(ventana, text=" ").grid(row=0, column=colcentral)
separador_2 = Label(ventana, text=" ").grid(row=2, column=colcentral)

#Botones
botonPublicar = Button(ventana, text="Publicar", command=ventanaPublicar)
botonPublicar.grid(row=1, column=1, sticky="news")
botonComentar = Button(ventana, text="Comentar", command=ventanaComentar)
botonComentar.grid(row=3, column=1, sticky="news")

botonLikear = Button(ventana, text="Dar Like", command=ventanaLikear)
botonLikear.grid(row=1, column=3, sticky="news")
botonCompartir = Button(ventana, text="Compartir", command=ventanaCompartir)
botonCompartir.grid(row=3, column=3, sticky="news")

# Expandir columnas hasta el borde (laterales)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)
ventana.grid_columnconfigure(4, weight=1)

# Bucle
ventana.mainloop()