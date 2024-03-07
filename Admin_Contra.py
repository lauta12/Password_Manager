#importando las cosas
import os
from os import mkdir
import secrets
import string
import platform
import pyperclip as cb

#Creo el generador de contraseñas seguras
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
abc = letters + digits + string.punctuation
pass_length = 42
password = ''
for i in range(pass_length):
    password += ''.join(secrets.choice(abc))

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
nombre_archivo = input(str("ingrese nombre del archivo txt: "))

#Guardo y creo el documento de texto
ruta_completa = os.path.join(path, f"{nombre_archivo}.txt")
gmail = input("Ingrese tu gmail, si no hay, apreta enter XD: ")
Nombre_de_usuario = input("Ingrese su nombre de usuario, si no hay, apreta enter XD: ")

with open(ruta_completa, "w") as f:
    f.write(gmail + "\n\n" + Nombre_de_usuario + "\n\n\n" + password)



# Abro el archivo de texto dependiendo del sistema operativo
if OS == "Windows":
    os.startfile(ruta_completa)
elif OS == "Linux":
    opener = "xdg-open" if os.path.exists("/usr/bin/xdg-open") else "gnome-open"
    os.system(f"{opener} {ruta_completa}")
else:
    print("No se pudo determinar el sistema operativo.")

#Escribo los datos guardados
f.write(gmail)
f.write("\n\n" + Nombre_de_usuario)
f.write("\n\n\n" + password)
f.close()
f = open(path + f'{nombre_archivo}.txt', 'r')
cb.copy(password)
