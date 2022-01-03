def meses_faltantes(numero):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[numero:]   #Con esto indicamos a python que nos devuelva una tupla con los valores siguientes al numero indicado

def meses_intermedios(inicio,final):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[inicio:final]

def meses_pasados(valor):
    meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
    return meses[:valor]

#Main
#Se recupera desde el mes indicado hasta el final de la lista
print("Imprimir los nombres de meses que faltan para fin de ano")
numero=int(input("Ingrese el numero de mes: "))
mesesfalta=meses_faltantes(numero)
print(mesesfalta)
######################################################################
inicio=int(input("Ingrese el valor inicial: "))
final=int(input("Ingrese el valor final: "))
mesesintermedios=meses_intermedios(inicio,final)
print("\n\nImprimir los meses intermedios")
print(mesesintermedios)
######################################################################
print("Imprime los meses que ya pasaron: ")
valor=int(input("Ingrese el numero de mes: "))
mesespasados=meses_pasados(valor)
print(mesespasados)