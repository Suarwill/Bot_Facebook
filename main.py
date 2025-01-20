import importlib as ilib
import subprocess as sub
def libSetup(lib):
    # Funcion para instalar automaticamente librerias no existentes
    try:ilib.import_module(lib)
    except ImportError:sub.check_call(['pip', 'install', lib])
import os, time, csv, datetime
libSetup('tkinter')
from tkinter import *
import tkinter.ttk as ttk
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
    ventanaConfigurar = Toplevel(ventana)
    ventanaConfigurar.title("Configuraciones")

    # Geometria
    width, heigth = 300, 200
    puntoMedioAnchura = int((ventanaConfigurar.winfo_screenwidth()-width)/4)
    puntoMedioAlto = int((ventanaConfigurar.winfo_screenheight()-heigth)/4)
    ventanaConfigurar.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")
    
    user_label = Label(ventanaConfigurar, text="Usuario: ")
    user_label.grid(row=0, column=0, padx=5, pady=5)
    user_entry = Entry(ventanaConfigurar, width=30)
    user_entry.grid(row=0, column=1, padx=5, pady=5)
    
    pass_label = Label(ventanaConfigurar, text="Contraseña: ")
    pass_label.grid(row=1, column=0, padx=5, pady=5)
    pass_entry = Entry(ventanaConfigurar, width=30)
    pass_entry.grid(row=1, column=1, padx=5, pady=5)

    def guardar():
        user = user_entry.get()
        password = pass_entry.get()
        if os.path.exists('.env'):
            load_dotenv()
        set_key(".env", "FACEBOOK_USERNAME", user)
        set_key(".env", "FACEBOOK_PASSWORD", password)
        print("Archivos actualizados con éxito.")
    
    guardar_button = Button(ventanaConfigurar, text="Guardar", command=guardar)
    guardar_button.grid(row=5, column=1, columnspan=2, pady=10)

def ventanaPublicar():
    ventanaPublicar = Toplevel(ventana)
    ventanaPublicar.title("Spam de Publicacion")

    width, heigth = 300, 400
    puntoMedioAnchura = int((ventanaPublicar.winfo_screenwidth()-width)/4)
    puntoMedioAlto = int((ventanaPublicar.winfo_screenheight()-heigth)/4)
    ventanaPublicar.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

    # Recuadro para el post
    post_label = Label(ventanaPublicar, text="Post:")
    post_label.grid(row=0, column=0, padx=5, pady=5)
    post_entry = Text(ventanaPublicar, width=30, height=8)
    post_entry.grid(row=0, column=1, padx=5, pady=5)

    # Recuadro para el link
    link_label = Label(ventanaPublicar, text="Link:")
    link_label.grid(row=1, column=0, padx=5, pady=5)
    link_entry = Entry(ventanaPublicar, width=30)
    link_entry.grid(row=1, column=1, padx=5, pady=5)

    post = docTXT("/Post.txt")
    post_entry.insert("1.0", post)
    link = docTXT("LinkImagenInternet.txt")
    link_entry.insert(0, link)

    def guardar_texto():
        post = post_entry.get("1.0", "end-1c")
        link = link_entry.get()
        with open("./Publicacion/Post.txt", "w", encoding="utf-8") as contenido:
            contenido.write(post)
        with open("./Publicacion/LinkImagenInternet.txt", "w", encoding="utf-8") as enlace:
            enlace.write(link)
        return print("Archivos actualizados con éxito.")

    guardar_button = Button(ventanaPublicar, text="Guardar", command=guardar_texto)
    guardar_button.grid(row=2, column=1, columnspan=1, pady=10)
    publicar_button = Button(ventanaPublicar, text="Publicar", command=publicar)
    publicar_button.grid(row=3, column=1, columnspan=1, pady=5)

def ventanaLikear():
    ventanaLikear = Toplevel(ventana)
    ventanaLikear.title("Dar Like")

    # Geometria
    width, heigth = 200, 150
    puntoMedioAnchura = int((ventanaLikear.winfo_screenwidth()-width)/4)
    puntoMedioAlto = int((ventanaLikear.winfo_screenheight()-heigth)/4)
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
    options = Options()
    chrome_profile_path = os.path.expandvars(os.getenv("PERFIL_CHROME"))
    options.add_argument("--disable-notifications")
    options.add_argument(f"user-data-dir={chrome_profile_path}")
    driver = webdriver.Chrome(options=options)
    AccesoWEB(driver)
        
    now = datetime.datetime.now()
    current_hour = now.hour

    web = "https://www.facebook.com/groups/"
    objetivos = docCSV('./Objetivos/Grupos.csv')

    if current_hour > 19 or current_hour < 4:
        saludo = "Buenas noches"
    elif current_hour > 12:
        saludo = "Buenas tardes"
    else:
        saludo = "Buen dia"
    post = docTXT("Post.txt")
    link = docTXT("LinkImagenInternet.txt")
    mensaje = (f"{saludo},\n{post}.\n{link}")
    print(mensaje)

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
            print(e)
    print("publicaciones realizadas")
    driver.quit()
        
def compartir():
    # funcion de comentar
    # ajustando
    return print("compartido")

def creacionEntorno():
    if not os.path.exists(".env"):
        with open(".env", "w") as env_file:
            env_file.write("FACEBOOK_USERNAME=\n")
            env_file.write("FACEBOOK_PASSWORD=\n")
            chrome = "%APPDATA%/Google/Chrome"
            env_file.write(f"PERFIL_CHROME={chrome}")

    if not os.path.exists("Objetivos"):
        os.makedirs("Objetivos")
    if not os.path.exists("Publicacion"):
        os.makedirs("Publicacion")

    if not os.path.exists("Objetivos/Grupos.csv"):
        with open("Objetivos/Grupos.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Grupo1"])

    if not os.path.exists("Publicacion/Post.txt"):
        open("Publicacion/Post.txt", "w").close()
    if not os.path.exists("Publicacion/LinkImagenInternet.txt"):
        open("Publicacion/LinkImagenInternet.txt", "w").close()
        print("entorno creado!")
    return 

def AccesoWEB(driver):
    web = "https://www.facebook.com"
    login = "/login/"
    userF = os.getenv("FACEBOOK_USERNAME")
    print(userF)
    passF = os.getenv("FACEBOOK_PASSWORD")
    print(passF)
    try:
        driver.get(web+login)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email")))
        username_field.send_keys(userF)
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "pass")))
        password_field.send_keys(passF)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "loginbutton")))
        login_button.click()
        time.sleep(50)
    except:
        print("continuando...")
    return

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
ventana.title("Bot de Facebook")
warnings.filterwarnings("ignore", category=UserWarning)

# Configuración de tamaño y posición de la ventana
width, heigth = 400, 300
puntoMedioAnchura = int((ventana.winfo_screenwidth()-width)/2)
puntoMedioAlto = int((ventana.winfo_screenheight()-heigth)/2)
ventana.geometry(f"{width}x{heigth}+{puntoMedioAnchura}+{puntoMedioAlto}")

#Etiquetas
for x in [0,2,4]:
    separador = Label(ventana, text=" ").grid(row=x, column=x)

#Botones
botonPublicar = Button(ventana, text="Publicar", command=ventanaPublicar, background= "lightblue")
botonPublicar.grid(row=1, column=1, sticky="news")
botonComentar = Button(ventana, text="Comentar", command=ventanaComentar, background= "lightblue")
botonComentar.grid(row=3, column=1, sticky="news")

botonLikear = Button(ventana, text="Dar Like", command=ventanaLikear, background= "lightblue")
botonLikear.grid(row=1, column=3, sticky="news")
botonCompartir = Button(ventana, text="Compartir", command=ventanaCompartir, background= "lightblue")
botonCompartir.grid(row=3, column=3, sticky="news")

botonCompartir = Button(ventana, text="⚙ Cfg.", command=ventanaConfigurar, background= "lightblue")
botonCompartir.grid(row=5, column=3, sticky="news")


# Expandir columnas hasta el borde (laterales)
for x in range(0,5):
    ventana.grid_columnconfigure(x, weight=1)

load_dotenv()
creacionEntorno()

# Bucle
ventana.mainloop()

# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ #
# Crear Paquete EXE                                               #
# pyinstaller --onefile main.py                                   #
# ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ #