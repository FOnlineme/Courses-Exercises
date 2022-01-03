import random

def cargar():
    lista=[]
    for x in range (10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)

#Main
lista=cargar()
print("La lista generada aleatoriamente es:")
imprimir(lista)
mezclar(lista)
print("La lista luego de mezclar es:")
imprimir(lista)