#Listas o Strings
'''
Ejemplo de string o lista
lista[2,3,"Carlos"]

    Para cambiar un componenete de la lista, lo seleccionamos mediante su sub-indice
    lista[3]="cambio"

    Para agregar un nodo al final de la lista se utiliza el operador append()
    lista.append(23)

    Para insertar un elemento en una posicion determinada de la lista y desplazar un elemento que este en esa
    posicion se utiliza el operador insert()
    lista.insert(2,76) #insertamos el 76 en la posicion 2

    Para eliminar un valor de la lista se utiliza el operador remove()
    lista.remove(2)

    Para buscar un valor de la lista se utiliza el operador in
    23 in lista

    Para saber la posicion de un valor en una lista se utiliza el operador index()
    lista.index(3)
'''

lista=[] #Declaramos una lista
for k in range(10):
    lista.append(input("Introduce un valor en la lista: "))

print("Los elementos de la lista son: " + str(lista)) #visualizamos los elementos de la lista
valor=int(input("Introduce el valor del indice a modificar: ")) #indice a modificar
nuevo=input("Introduce el nuevo valor: ") #valor nuevo de indice que se modifica
lista[valor]=nuevo #realizamos la modificacion
print("Los elementos de la lista son: " + str(lista)) #visualizamos la lista modificada

valor=int(input("Introduce el siguiente indice en el que se insertara el nuevo valor: ")) #indice donde se insertara el nuevo valor
nuevo=input("Introduce el nuevo valor: ") #valor a insertar
lista.insert(valor, nuevo)
print("Los elementos de la lista son: " + str(lista)) #visualizamos la lista modificada

nuevo=input("Introduce el valor a eliminar: ")
lista.remove(nuevo) #eliminamos el valor
print("Los elementos de la lista son: " + str(lista)) #visualizamos la lista modificada

nuevo=input("Introduce el valor a buscar: ")
resultado=(nuevo in lista)
if resultado:
    print("Existe este elemento y su indice es: " + str(lista.index(nuevo)))
else:
    print("No existe este elemento")