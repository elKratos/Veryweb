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
        hash_path = "web/hash.txt"
        actual_hash = hashing(path)
        
        if os.path.isfile(hash_path):
            with open(hash_path, 'rb') as hf:
                if hf.read() != actual_hash:
                    is_change = True
        else:
            with open(hash_path, "w") as txt:
                txt.write(actual_hash)
                deleteFile(path)

    else:
        print("Ha ocurrido un error al crear el archivo.")
        break

if is_change: pass