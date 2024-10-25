#-utf8

import wget
import time
import difflib
import os
import hashlib

# TODO: Realiza una aplicación que compruebe cada 30 segundos si hay algún cambio en una página web. Si existe el cambio, muestra las diferencias y para su ejecución.
# TODO: Puedes mejorar este programa enviando las diferencias por correo electrónico.

# Esperamos 30 segundos
def witing(): time.sleep(30)

# TODO: Descargar el codigo de la web
def download_web(url): 
    os.makedirs("web", exist_ok=True)
    path = 'web/fontcode.html'
    
    wget.download(url, path)

    return path

# Eliminamos el archivo
def deleteFile(url):
    file = os.path.join("web", os.path.basename(url))
    os.remove(file)

# Obtener el hash del archivo
def hashing(file_path): 
    file = open(file_path, 'rb')
    return hashlib.sha256(file.read()).hexdigest()
 
is_change=False

while not is_change:
    path = download_web("https://fs2ps.festeweb.com/")
    
    if os.path.isfile(path):
        h = hashing(path)

        if os.path.isfile("hash"):
            #TODO: Comparamos hash almacenado con el obtenido
            pass
        
        else:
            # Creamos el archivo
            with open("web", "w") as txt:
                txt.write(h)

    else:
        print("Ha ocurrido un error al crear el archivo.")
        break

if is_change: pass