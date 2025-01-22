import importlib as ilib
import subprocess as sub
def libSetup(lib):
    # Funcion para instalar automaticamente librerias no existentes
    try:ilib.import_module(lib)
    except ImportError:sub.check_call(['pip', 'install', lib])

import os, time, csv, datetime
libSetup('tkinter')
from tkinter import *
libSetup('warnings')
import warnings
libSetup('python-dotenv')
from dotenv import load_dotenv, set_key
libSetup('selenium')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def ventanaConfigurar():
    load_dotenv(override=True)
    ventanaConfigurar = Toplevel(ventana)
    crearVentana(ventanaConfigurar,"Configuraciones",300,200)
    
    userLabel = Label(ventanaConfigurar, text="Usuario: ")
    userLabel.grid(row=0, column=0, padx=5, pady=5)
    userDato = Entry(ventanaConfigurar, width=30)
    userDato.grid(row=0, column=1, padx=5, pady=5)
    
    passLabel = Label(ventanaConfigurar, text="Contraseña: ")
    passLabel.grid(row=1, column=0, padx=5, pady=5)
    passDato = Entry(ventanaConfigurar, width=30)
    passDato.grid(row=1, column=1, padx=5, pady=5)

    user = codec(os.getenv("FACEBOOK_USERNAME"),False)
    userDato.insert(0,user)
    pasw = codec(os.getenv("FACEBOOK_PASSWORD"),False)
    passDato.insert(0,pasw)

    def guardar():
        user = codec(userDato.get())
        password = codec(passDato.get())
        if os.path.exists('.env'):
            set_key(".env", "FACEBOOK_USERNAME", user)
            set_key(".env", "FACEBOOK_PASSWORD", password)
        print("Archivos actualizados con éxito.")
        return ventanaConfigurar.destroy()
    
    botonGuardar = Button(ventanaConfigurar, text="Guardar", command=guardar)
    botonGuardar.grid(row=5, column=1, columnspan=2, pady=10)

    ventanaConfigurar.mainloop()

def ventanaPublicar():
    ventanaPublicar = Toplevel(ventana)
    crearVentana(ventanaPublicar,"Spam de Publicacion",500,400)
    filaInicial = 0

    # Recuadro para el titulo
    tituloLabel = Label(ventanaPublicar, text="Archivo:")
    tituloLabel.grid(row=filaInicial, column=0, padx=5, pady=5)
    tituloEntry = Text(ventanaPublicar, width=30, height=1)
    tituloEntry.grid(row=filaInicial, column=1, padx=5, pady=5)

    # Recuadro para el post
    postLabel = Label(ventanaPublicar, text="Post:")
    postLabel.grid(row=filaInicial+1, column=0, padx=5, pady=5)
    postEntry = Text(ventanaPublicar, width=30, height=10)
    postEntry.grid(row=filaInicial+1, column=1, padx=5, pady=5)

    # Recuadro para el link
    linkLabel = Label(ventanaPublicar, text="Le recomiendo insertar un link hacia su aviso con fotos, al final del texto")
    linkLabel.grid(row=filaInicial+2, column=1, padx=5, pady=5)

    # Selector de publicaciones
    publicaciones_label = Label(ventanaPublicar, text="Publicaciones Guardadas:")
    publicaciones_label.grid(row=filaInicial+3, column=0, padx=5, pady=5)

    # Obtener lista de publicaciones guardadas
    lista_publicaciones = os.listdir("./Publicacion") 
    lista_publicaciones = [f for f in lista_publicaciones if f.endswith(".txt")] 

    # Crear lista desplegable
    publicaciones_var = StringVar(ventanaPublicar)
    publicaciones_var.set(lista_publicaciones[0])  # Seleccionar la primera publicación por defecto
    publicaciones_menu = OptionMenu(ventanaPublicar, publicaciones_var, *lista_publicaciones)
    publicaciones_menu.grid(row=filaInicial+3, column=1, padx=5, pady=5)

    def cargar_publicacion():
        seleccionada = publicaciones_var.get()
        with open(f"./Publicacion/{seleccionada}", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        if seleccionada.startswith("Post"):
            postEntry.delete("1.0", END)
            postEntry.insert("1.0", contenido)

    cargar_button = Button(ventanaPublicar, text="Cargar", command=cargar_publicacion)
    cargar_button.grid(row=filaInicial+3, column=2, padx=5, pady=5)

    def guardar_texto(tituloEntry, postEntry):
        with open(f"./Publicacion/Post{tituloEntry.get("1.0", "end-1c")}.txt", "w", encoding="utf-8") as contenido:
            contenido.write(postEntry.get("1.0", "end-1c"))
        return print("Archivos actualizados con éxito.")

    guardar_button = Button(ventanaPublicar, text="Guardar", command=lambda  : guardar_texto(tituloEntry, postEntry) )
    guardar_button.grid(row=filaInicial+6, column=1, columnspan=1, pady=5)
    publicar_button = Button(ventanaPublicar, text="Publicar", command=publicar)
    publicar_button.grid(row=filaInicial+7, column=1, columnspan=1, pady=5)

def ventanaGrupo():
    ventanaGrupo = Toplevel(ventana)
    crearVentana(ventanaGrupo,"Agregar Grupo",300,500)
    texto_label = Label(ventanaGrupo, text="Texto:")
    texto_label.grid(row=0, column=0)
    texto_entry = Entry(ventanaGrupo)
    texto_entry.grid(row=0, column=1)

    # Botón "Empezar"
    empezar_button = Button(ventanaGrupo, text="Empezar", command=lambda: likear(texto_entry.get()))
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
    options = Options()
    chrome_profile_path = os.path.expandvars(os.getenv("PERFIL_CHROME"))
    options.add_argument("--disable-notifications")
    options.add_argument(f"user-data-dir={chrome_profile_path}")

    driver = webdriver.Chrome(options=options)
    AccesoWEB(driver)
    web = "https://www.facebook.com/groups/"
    objetivos = docCSV('./Objetivos/Grupos.csv')

    now = datetime.datetime.now()
    horaActual = now.hour
    if horaActual > 19 or horaActual < 4:
        saludo = "Buenas noches"
    elif horaActual > 12:
        saludo = "Buenas tardes"
    else:
        saludo = "Buen dia"

    post = docTXT("Post.txt")
    mensaje = (f"{saludo},\n{post}.\n")

    for x in objetivos:
        driver.get(web+x)
        try:
            botonPost  = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Escribe algo...']")))
            botonPost.click()
            time.sleep(2)
            cajaPost  = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-offset-key]")))
            cajaPost.send_keys(mensaje)
            botonPublicar  = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//span[text()='Publicar']")))
            botonPublicar.click()
            print(f"publicacion realizada en: {x}")
        except (NoSuchElementException, TimeoutException) as e:
            print(f"No se pudo realizar publicacion. \nError: {e}")
            continue

    print("publicaciones realizadas")
    driver.quit()
        
def compartir():
    # funcion de comentar
    # ajustando
    return print("compartido")

def creacionEntorno():
    def crearCarpeta(nombre):
        if not os.path.exists(nombre):
            os.makedirs(nombre)

    if not os.path.exists(".env"):
        with open(".env", "w") as env_file:
            chrome = "%APPDATA%/Google/Chrome"
            env_file.write("FACEBOOK_USERNAME=\n")
            env_file.write("FACEBOOK_PASSWORD=\n")
            env_file.write(f"PERFIL_CHROME={chrome}")

    crearCarpeta("Objetivos")
    crearCarpeta("Publicacion")

    if not os.path.exists("Objetivos/Grupos.csv"):
        with open("Objetivos/Grupos.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["ID_grupo,Titulo_del_grupo"])

    if not os.path.exists("Publicacion/Post.txt"):
        open("Publicacion/Post.txt", "w").close()

    return print("entorno creado!")

def crearVentana(ventana,titulo,width,heigth):
    # Configuración de tamaño y posición de la ventana
    ventana.title(titulo)
    puntoMedioAnchura = int((ventana.winfo_screenwidth()-width)/2)
    puntoMedioAlto = int((ventana.winfo_screenheight()-heigth)/2)
    ventana.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

def AccesoWEB(driver):
    web = "https://www.facebook.com"
    login = "/login/"
    load_dotenv(override=True)
    dato1 = codec(os.getenv("FACEBOOK_USERNAME"),False)
    dato2 = codec(os.getenv("FACEBOOK_PASSWORD"),False)
    try:
        driver.get(web+login)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
        username_field.send_keys(dato1)
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pass")))
        password_field.send_keys(dato2)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loginbutton")))
        login_button.click()
        print("Dispones de 50 segundos para hacer la verificacion de 2 pasos de la página.")
        time.sleep(50)
    except:
        print("continuando...")
    return

def codec(w, cif=True):
    x , i = "" , 1
    for c in w:
        y = ord(c)
        if cif : nV = (y+i)%256
        else: nV = (y-i)%256
        i += 1
        nV = max(0, min(nV, 0x10FFFF))
        nC = chr(nV)
        x += nC
    return x

def docCSV(documento):
    with open(documento, 'r') as csvfile:
        reader = csv.reader(csvfile)
        listado = {row[0]: row[0] for row in reader}
    return listado

def docTXT(link):
    try:
        with open(f"./Publicacion/{link}", "r", encoding="utf-8") as texto:
            archivo = texto.read()
    except FileNotFoundError:
        print(f"Error: {link} no existe.")
        archivo = ""
    return archivo

# Inicio de GUI
ventana = Tk()
warnings.filterwarnings("ignore", category=UserWarning)

crearVentana(ventana,"Bot de Facebook",500,400)
creacionEntorno()
load_dotenv()

#Etiquetas
for x in [0,2,4]:
    separador = Label(ventana, text=" ").grid(row=x, column=x)

#Botones
botonPublicar = Button(ventana, text="Publicar", command=ventanaPublicar, background= "lightblue")
botonPublicar.grid(row=1, column=1, sticky="news")
botonComentar = Button(ventana, text="Comentar", command=ventanaComentar, background= "lightblue")
botonComentar.grid(row=3, column=1, sticky="news")

botonLikear = Button(ventana, text="Dar Like", command=ventanaGrupo, background= "lightblue")
botonLikear.grid(row=1, column=3, sticky="news")
botonCompartir = Button(ventana, text="Compartir", command=ventanaCompartir, background= "lightblue")
botonCompartir.grid(row=3, column=3, sticky="news")

botonCompartir = Button(ventana, text="⚙ Cfg.", command=ventanaConfigurar, background= "lightblue")
botonCompartir.grid(row=5, column=3, sticky="news")

# Expandir columnas hasta el borde (laterales)
for x in range(0,5):
    ventana.grid_columnconfigure(x, weight=1)

# Bucle
ventana.mainloop()

# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ #
# Crear Paquete EXE                                               #
# pyinstaller --onefile main.py                                   #
# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ #