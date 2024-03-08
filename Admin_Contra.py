#importando las cosas
import os
from os import mkdir
import secrets
import string
import platform
import pyperclip as cb



#Obtengo el nombre del sistema operativo
OS = platform.uname()[0]
#obtengo el nombre de usuario del sistema operativo
username = os.getlogin()

if OS == "Linux":

    #Asigno la ruta
    path = f"/home/{username}/Desktop/AUTOPLAY2/"

    #Comparo que no exista el archivo, si no existe se crea
    if os.path.isdir(f"/home/{username}/Desktop/AUTOPLAY2") == False:
        mkdir(f"/home/{username}/Desktop/AUTOPLAY2")
   

if OS == "Windows":

    path = f"C:/Users/{username}/Desktop/AUTOPLAY2/"
    #Comparo que no exista el archivo, si no existe se crea
    if os.path.isdir(f"C:/Users/{username}/Desktop/AUTOPLAY2") == False:
        mkdir(f"C:/Users/{username}/Desktop/AUTOPLAY2")
    else:
        pass

#Creo el nombre del archivo
nombre_archivo = input(str("type the name of the txt file: "))

#Guardo y creo el documento de texto
ruta_completa = os.path.join(path, f"{nombre_archivo}.txt")
gmail = input("Type your email: ")
Nombre_de_usuario = input("Type your username (if its not required press 'enter'): ")
pass_length = input("Type how many characters your password will have: ")

#Creo el generador de contraseñas seguras
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
abc = letters + digits + string.punctuation
password = ''

for i in range(int(pass_length)):
    password += ''.join(secrets.choice(abc))

with open(ruta_completa, "w") as f:
    f.write(gmail + "\n\n" + Nombre_de_usuario + "\n\n\n" + password)


# Abro el archivo de texto dependiendo del sistema operativo
if OS == "Windows":
    os.startfile(ruta_completa)
elif OS == "Linux":
    opener = "xdg-open" if os.path.exists("/usr/bin/xdg-open") else "gnome-open"
    os.system(f"{opener} {ruta_completa}")
else:
    print("Your operative system cannot be determined")

#guardo la contraseña al portapapeles
cb.copy(password)

