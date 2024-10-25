# Veryweb
A web changes verificator

Hoja de ruta:
1. Descargar y almacenar la pagina web
2. Sacar el hash de el archivo que hemos descargado
3. Comprobar si tenemos un hash almacenado
    3.1. Si no lo tenemos lo almacenamos en un archivo llamado hash
    3.2. Si lo tenemos, lo comparamos para ver si son iguales
4. Si son iguales, volvemos al punto 1 despues de 30 segundos
5. Si no son iguales:
    5.1. Guardamos el nuevo hash
    5.2. Vemos que ha cambiado
    5.3. Enviamos los cambios por correo

Dependency:
pip install wget