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
def download_web(url): pass

# Obtener el hash del archivo
def hashing(file_path): 
    file = open(file_path, 'rb')
    return hashlib.sha256(file.read()).hexdigest()

# TODO: El comparar hash. 
#       Tenemos un hash guardado? No, lo guardamos. Si, los comparamos.
#       El hash es igual? Si, seguimos. No, paramos de descargar y buscamos el cambio.

# TODO: Comparamos el codigo fuente y sacamos la diferencia.

# TODO: Obtenemos la diferencia y la enviamos por correo.

# TODO: Detenemos la aplicacion
    

print(hashing("index.html"))