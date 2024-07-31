import os
import secrets
import string
import platform
import pyperclip as pc

def Get_Os_Path(OS):
    if OS == "Windows":
        path = f"C:/Users/OneDrive/{username}/Desktop/AUTOPLAY2/"
        #Comparo que no exista el archivo, si no existe se crea
        if not os.path.isdir(f"C:/Users/OneDrive/{username}/Desktop/AUTOPLAY2"):
            os.mkdirs(path)
    else:
        path = f"/home/{username}/Desktop/AUTOPLAY2/"
    return path
#Cambia la ruta absoluta dependiendo el sistema operativo
def OpenFile(OS):
    if OS == "Windows":
        os.startfile(path)
    elif OS == "Linux":
        opener = "xdg-open" if os.path.exists("/usr/bin/xdg-open") else "gnome-open"
        os.system(f"{opener} {path}")
    else:
        print("Your operative system cannot be determined")

def Pass_Gen(pass_length):
    #Creo el generador de contraseñas seguras
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    abc = letters + digits + string.punctuation
    password = ''

    for i in range(int(pass_length)):
        password += ''.join(secrets.choice(abc))
    return password

#Nombre del sistema operativo
OS = platform.uname()[0]
#Nombre de usuario del sistema operativo
username = os.getlogin()
#ruta del sistema operativo
path = Get_Os_Path(OS)

#Creo el nombre del archivo
nombre_archivo = input(str("type the name of the file: (without \".txt\") "))
#Guardo y creo el documento de texto
path = os.path.join(path, f"{nombre_archivo}.txt")
gmail = input("Type your email: ")
Nombre_de_usuario = input("Type your username (If it isn't required press 'ENTER'): ")
pass_length = input("Type how many characters you want your password to be: ")

password = Pass_Gen(pass_length)

with open(path, "w") as f:
    f.write(gmail + "\n\n" + Nombre_de_usuario + "\n\n\n" + password)

# Abro el archivo de texto dependiendo del sistema operativo
OpenFile(OS)

#guardo la contraseña al portapapeles
pc.copy(password)
