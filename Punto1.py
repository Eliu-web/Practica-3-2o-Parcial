print (" ")#Espacio de linea
print ("Velazquez Mares Jesus Eliu 3W  1276")
print (" ")#Espacio de linea

#Creacion del diccionario
dic = {
    'Euro':'€',
    'Dollar':'$', 
    'Yen':'¥'
}

qwer = str(input("Ingresa una divisa: "))#Guarda la divisa que el usuario ingresa
if qwer in dic: #si la variable qwer esta en el diccionario dic
    print (dic[qwer])#imprime en pantalla el simbolo
else: #sino
    print ("Favor de ingresar una divisa valida")#imprime en pantalla un mensaje de error