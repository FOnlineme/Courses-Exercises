nota1=int(input("Ingrese primer nota: "))
nota2=int(input("Ingrese segunda nota: "))
nota3=int(input("Ingrese tercer nota: "))
notaT=(nota1+nota2+nota3)/3

if notaT>=7 :
    print("Promocionado, " + "con la nota: " + str(notaT))
else:
    if notaT >= 4:
        print("Regular, " + "con la nota: " + str(notaT))
    else:
        print("Libre, " + "con la nota: " + str(notaT))

#Para agregar un else con condicion se usa la sentencia "elif"