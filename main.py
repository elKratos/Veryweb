#-utf8

import wget
import time
import difflib
import os
import hashlib

# TODO: Realiza una aplicación que compruebe cada 30 segundos si hay algún cambio en una página web. Si existe el cambio, muestra las diferencias y para su ejecución.
# TODO: Puedes mejorar este programa enviando las diferencias por correo electrónico.

# Esperamos 30 segundos
def waiting(tics=30): time.sleep(tics)

# TODO: Descargar el codigo de la web
def download_web(url): 
    os.makedirs("web", exist_ok=True)
    path = 'web/code_downloaded.html'
    
    wget.download(url, path)

    return path

# Eliminamos el archivo
def deleteFile(file): 
    os.remove(file)

# Obtener el hash del archivo
def hashing(file_path): 
    with open(file_path, 'rb') as fp:
        return hashlib.sha256(fp.read()).hexdigest()
    
def reader(path):
    with open(hash_path, 'r', encoding='utf-8') as f:
        return str(f.read())

def writer(path, value):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(value)


is_change=False

while not is_change:
    path = download_web("https://www.example.com/")
    
    if os.path.isfile(path):
        hash_path = "web/hash.txt"
        actual_hash = hashing(path)
        
        if os.path.isfile(hash_path):
            save_hash = reader(hash_path)
            if save_hash != actual_hash:
                # TODO: Guardamos el nuevo codigo para compararlo. (code_save2.html)
                writer(hash_path, actual_hash)
                is_change = True
            
            else:
                # TODO: Borramos el codigo guardado.
                pass

        else:
            writer(hash_path, actual_hash)
            # TODO Guardamos el codigo actual (code_save1.html)

        deleteFile(path)
        waiting(10)
        #waiting(30)

    else:
        print("Ha ocurrido un error al crear el archivo.")
        break

if is_change: 
    # TODO: Comprobar que ha cambiado del archivo
    pass