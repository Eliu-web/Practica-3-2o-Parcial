print (" ")#Espacio de linea
print ("Velazquez Mares Jesus Eliu 3W  1276")
print (" ")#Espacio de linea

#Creacion del diccionario
dic = {
    'melon':4.5,
    'sandia':7.8,
    'manzana':3.4
}
#Preguntamos al usuario que fruta desea comprar y lo guardamos en una variable
f = input("Ingresa el nombre de la fruta a comprar: ").lower()
#Preguntamos al usuario que cantidad de kilos de fruta desea llavar y lo guardamos en una variable
k = float(input("Ingresa la cantidad de fruta en kilos que deseas llevar: "))
#si la variable f esta en el diccionario entonces
if f in dic:
#muestra en pantalla lo sigiente
    print (k, "de", f, "son unos", dic[f] * k,"$")
#sino
else:
#imprime en pantalla un mesaje de error
    print ("No contamos con esta fruta.")




