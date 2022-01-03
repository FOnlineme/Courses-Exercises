archivo = open("archivo.txt", "w+")
seleccion=input("Introduce el texto para agregar al archivo: ")

contenido = archivo.read()
final_de_archivo=archivo.tell()

archivo.write(seleccion)
archivo.seek(final_de_archivo)
nuevo_contenido=archivo.read()

archivo.close()

print("El contenido antes de agregar cosas es:", contenido)
print("El contenido despues de agregar cosas es:", nuevo_contenido)
