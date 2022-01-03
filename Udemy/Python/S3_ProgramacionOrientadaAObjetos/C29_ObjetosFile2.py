archivo=open("archivo.txt", "r+")
contenido=archivo.read()
final_de_archivo=archivo.tell()
lista = ['Linea 1\n','Linea 2']

archivo.writelines(lista)
archivo.seek(final_de_archivo)

print(archivo.readline())
print(archivo.readline())