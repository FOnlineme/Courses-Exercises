'''Un diccionario es un arreglo de elementos en donde el indice de busqueda es una palabra'''

def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        castellano=input("Ingrese una palabra en castellano: ")
        ingles=input("Ingrese una palabra en ingles: ")
        diccionario[castellano]=ingles
        continua=input("Quiere cargar otra palabra: [s/n]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for k in diccionario:   #Recorro el diccionario con k
        print(k,diccionario[k])

def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en castellano a consultar: ")
    if pal in diccionario:
        print("En ingles significa:",diccionario[pal])


#main
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)