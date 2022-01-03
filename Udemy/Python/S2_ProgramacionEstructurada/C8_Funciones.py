def presentacion():
    print("\nPrograma para hacer operaciones aritmeticas de suma y resta de dos valores.")
    print("**************************************************************************\n")

def introducirDatos():
    global valor1
    global valor2
    valor1=int(input("Ingrese el primer valor: "))
    valor2=int(input("Ingrese el segundo valor: "))

def suma():
    suma= valor1 + valor2
    print("La suma de dos valores es: ", suma)

def resta():
    resta=valor1-valor2
    print("La resta de dos valores es: ", resta)

def finalizacion():
    print("\n**************************************************************************")
    print("Gracias por utilizar este programa\n")

#Main
presentacion()
introducirDatos()
suma()
resta()
finalizacion()