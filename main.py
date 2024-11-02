#-utf8

import wget
import time
import difflib
import os
import hashlib

PATH = 'web/'

# TODO: Realiza una aplicación que compruebe cada 30 segundos si hay algún cambio en una página web. Si existe el cambio, muestra las diferencias y para su ejecución.
# TODO: Puedes mejorar este programa enviando las diferencias por correo electrónico.

# Esperamos 30 segundos
def waiting(tics=30): time.sleep(tics)

# Descarga el codigo y devuelve la ruta donde esta almacenado.
def download_web(url): 
    # Crea la carpeta en caso de no existir donde almacenaremos el codigo.
    os.makedirs(PATH, exist_ok=True)

    # Creamos la ruta donde se almacenara el codigo que descargemos.
    path = PATH + 'code_downloaded.html'
    
    # Descargamos el codigo de la web que deseemos.
    wget.download(url, path)

    return path

# Eliminamos el archivo
def deleteFile(file): os.remove(file)

# Obtener el hash del archivo
def hashing(file_path): 
    with open(file_path, 'rb') as fp:
        return hashlib.sha256(fp.read()).hexdigest()
    
# Leemos un archivo y enviamos el contenido
def reader(path):
    with open(hash_path, 'r', encoding='utf-8') as f:
        return str(f.read())

# Creamos o sobrescrivimos un arcivo
def writer(path, value):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(value)


# Por defecto, aun no ha cambiado nada.
is_change=False

while not is_change:
    # Descargamos el cofigo de la web, y obtenemos la ruta donde se a almacenado.
    code_path = download_web("https://www.example.com/")
    
    # Comprobamos que se ha descargado un archivo.
    if os.path.isfile(code_path):
        # Creamos una ruta para crear el archivo que contendra el hash de la pagina descargada.
        hash_path = PATH + "hash.txt"

        # Obtenemos el hash de la pagina actual
        current_hash = hashing(code_path)
        
        # Si ya existe un hash.txt, lo comparamos
        if os.path.isfile(hash_path):
            # Obtenemos el hash anterior
            storage_hash = reader(hash_path)

            # Comparamos el hash actual con el almacenado.
            if storage_hash != current_hash:
                # Al ser distinto, almacenamos el nuevo codigo en un nuevo archivo.   
                os.rename(code_path, PATH + 'code_changed.html')  

                # Actualizamod el antiguo hash
                writer(hash_path, current_hash) 
                
                # Confirmamos que el codigo ha cambiado.
                is_change = True

        # Si no existe, lo creamos, y almacenamos el codigo descargado y el hash de este.
        else:
            os.rename(code_path, PATH + 'code_storage.html')
            writer(hash_path, current_hash)

        deleteFile(code_path)
        waiting(10)
        #waiting(30)

    # En caso de no encontrarlo, ha ocurrido un error.
    else:
        print("Ha ocurrido un error al crear o descargar el archivo.")
        break

if is_change: 
    # TODO: Comprobar que ha cambiado del archivo
    pass