print (" ")#Espacio de linea
print ("Velazquez Mares Jesus Eliu 3W  1276")
print (" ")#Espacio de linea

#Creacion del diccionario
dic = {
    'nombre':' ',
    'edad':' ',
    'direccion':' ',
    'telefono':' '
}
#el usuario ingresa el valor en el diccionario correspondiente
dic['nombre'] = str(input("Ingresa tu nombre completa: "))
dic['edad'] = int(input("Ingresa tu edad: "))
dic['direccion'] = int(input("Ingresa tu direccion: "))
dic['telefono'] = int(input("Ingresa tu numero telefonico: "))

#muestra en pantalla tus datos
print (dic['nombre'])
print("tiene" ,dic['edad'], "años,")
print ("vive en",dic['direccion'])
print ("y su número de teléfono es ",dic['telefono'])

