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
def delete_file(file): os.remove(file)

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

# Procesa y limpia el texto que vamos a mostrar
def clean_text(text, discard_char="", discard_lines=()):
    if text.startswith(discard_char):
        # Solo nos interesa mostrar el texto cambiado, por lo que descartamos otras que no son necesarias.
        if text.strip() not in discard_lines: 
            # Quitamos solo el caracter que queremos descartar (solo el primero)
            text = text.replace(discard_char, "", 1)
            # Devolvemos el texto quitando los espacios del inicio
            return text.lstrip(" ")
    
    return None


# Por defecto, aun no ha cambiado nada.
is_change=False

while not is_change:
    print("Descargando la web")
    waiting(3)

    # Descargamos el cofigo de la web, y obtenemos la ruta donde se a almacenado.
    # code_path = download_web("https://www.example.com/")
    code_path = download_web("https://www.lajarina.es/")
    
    
    print("\nWeb descargada en: " + code_path)

    # Comprobamos que se ha descargado un archivo.
    if os.path.isfile(code_path):
        # Creamos una ruta para crear el archivo que contendra el hash de la pagina descargada.
        hash_path = PATH + "hash.txt"

        print("Creando hash")
        waiting(2)

        # Obtenemos el hash de la pagina actual
        current_hash = hashing(code_path)
        
        print("Hash obtenido: " + current_hash)
        print("Buscando archivo hash.txt")
        waiting(3)

        # Si ya existe un hash.txt, lo comparamos
        if os.path.isfile(hash_path):
            print("Se ha detectado el archivo \"hash.txt\"")
            print("Obteninedo hash almacenado")
            # Obtenemos el hash anterior
            storage_hash = reader(hash_path)

            print("Hash: "+storage_hash+" \nComparando hashes")
            waiting(3)

            # Comparamos el hash actual con el almacenado.
            if storage_hash != current_hash:
                print("Se ha encontrado una diferencia. Almacenando cambios")

                # Al ser distinto, almacenamos el nuevo codigo en un nuevo archivo.   
                os.rename(code_path, PATH + 'code_changed.html')  
                
                # Confirmamos que el codigo ha cambiado.
                is_change = True

            else:
                print("No se ha encontrado diferencia: " + current_hash)

        # Si no existe, lo creamos, y almacenamos el codigo descargado y el hash de este.
        else:
            print("No se ha encontrado el arcihvo. \nCreando...")
            waiting(3)

            writer(hash_path, current_hash)
            print("Se ha creado corectamente")

            print("Almacenando codigo descargado como \"code_storaged.html\"")
            os.rename(code_path, PATH + 'code_storaged.html')
            print("Archivo guardado.")

        if os.path.isfile(code_path):
            print("Eliminando temporales.")
            delete_file(code_path)

        if not is_change:
            print("Esperando 30 segundos para volver a descargar...")
            waiting(30)

    # En caso de no encontrarlo, ha ocurrido un error.
    else:
        print("Ha ocurrido un error al crear o descargar el archivo.")
        break

# Si la web a cambiado, procedemos a mostrar los cambios.
if is_change: 
    print ("Mostrando cambios.")
    
    # Guardamos el codigo de la primera pagina
    with open(PATH + "code_storaged.html", 'r') as code:
        storaged = code.readlines()

    # Guardamos el codigo de la pagina cambiada
    with open(PATH + "code_changed.html", 'r') as code:
        changed = code.readlines()

    # Comparamos el texto y obtenemos las diferencias
    diff = difflib.unified_diff(storaged, changed)

    # Peparamos la salida de texto en el terminal
    after,before = "Antes:\n","Despues:\n"

    with open(PATH + "code_diff.txt", 'w') as f_out:
        # Procesamos de linea en linea
        for line in diff:
            # Escribimos las linas en una archivo para ver mejor las diferencias
            f_out.write(line)

            # Si la linea empieza por "-", es la linea como era antes de que cambiara. Procesamos el texto y lo almacenamos para mostrarlo mas adelante.
            clean_line = clean_text(line, "-", ("---"))
            if clean_line: after += clean_line

            # Si la linea empieza por "+", es la linea con los cambios añadidos. Procesamos el texto y lo almacenamos para mostrarlo mas adelante.
            clean_line = clean_text(line, "+", ("+++"))
            if clean_line: before += clean_line
            
        
        # Sacamos por terminal el texto que hemos preparado. Contiene las lineas antes y despues de que cambiaran.
        print(after + "\n\n" + before)