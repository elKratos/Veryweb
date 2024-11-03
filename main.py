#-utf8

import wget
import time
import difflib
import os
import hashlib

BASE_DIR = 'web/'

# Tiempo de espera
def timing(tics): time.sleep(tics)

# Obtener el hash del archivo
def hashing(file_path): 
    with open(file_path, 'rb') as fp:
        return hashlib.sha256(fp.read()).hexdigest()
    
# Leemos un archivo y enviamos el contenido
def reader(path):
    with open(path, 'r', encoding='utf-8') as f:
        return str(f.read())

# Creamos o sobrescrivimos un arcivo
def writer(path, value):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(value)

# Por defecto, aun no ha cambiado nada.
changes=False

while not changes:
    print("Descargando la web")
    timing(3)

    # Crea la carpeta en caso de no existir donde almacenaremos el codigo.
    os.makedirs(BASE_DIR, exist_ok=True)
    # Creamos la ruta donde se almacenara el codigo que descargemos.
    path = BASE_DIR + 'code_downloaded.html'
    # Descargamos el codigo de la web que deseemos.
    wget.download("https://tecmasupply.com/", path)

    print("\nWeb descargada en: " + path)

    # Comprobamos que se ha descargado un archivo.
    if os.path.isfile(path):
        # Creamos una ruta para crear el archivo que contendra el hash de la pagina descargada.
        hash_path = BASE_DIR + "hash.txt"

        print("Creando hash")

        # Obtenemos el hash de la pagina actual
        current_hash = hashing(path)
        
        print("Hash obtenido: " + current_hash)
        print("Buscando archivo hash.txt")

        # Si ya existe un hash.txt, lo comparamos
        if os.path.isfile(hash_path):
            print("Se ha detectado el archivo \"hash.txt\"")
            print("Obteninedo hash almacenado")
            # Obtenemos el hash anterior
            storage_hash = reader(hash_path)

            print("Hash: "+storage_hash+" \nComparando hashes")

            # Comparamos el hash actual con el almacenado.
            if storage_hash != current_hash:
                print("Se ha encontrado una diferencia. Almacenando cambios")

                # Al ser distinto, almacenamos el nuevo codigo en un nuevo archivo.   
                os.rename(path, BASE_DIR + 'code2.html')  
                
                # Confirmamos que el codigo ha cambiado.
                changes = True

            else:
                print("No se ha encontrado diferencia: " + current_hash)

        # Si no existe, lo creamos, y almacenamos el codigo descargado y el hash de este.
        else:
            print("No se ha encontrado el arcihvo. \nCreando...")

            writer(hash_path, current_hash)
            print("Se ha creado corectamente")

            print("Almacenando codigo descargado como \"code1.html\"")
            os.rename(path, BASE_DIR + 'code1.html')
            print("Archivo guardado.")

        if os.path.isfile(path):
            print("Eliminando temporales.")
            os.remove(path)

        if not changes:
            print("Esperando 30 segundos para volver a descargar...")
            timing(5)

    else:
        print("Ha ocurrido un error al crear o descargar el archivo.")
        break

if changes: 
    print ("Mostrando cambios.")
    after = "Antes:\n"
    before = "Despues:\n"
    
    with open(BASE_DIR + "code1.html", 'r') as code1, \
     open(BASE_DIR + "code2.html", 'r') as code2:
        text1 = code1.readlines()
        text2 = code2.readlines()

    diff = difflib.unified_diff(text1, text2)

    with open(BASE_DIR + "checksum.txt", 'w') as f_out:
        for line in diff:
            f_out.write(line)

            if line.startswith("-") and line.strip() != "---":
                after += line[1:].lstrip()

            if line.startswith("+") and line.strip() != "+++":
                before += line[1:].lstrip()
        
        print(after + "\n\n" + before)
