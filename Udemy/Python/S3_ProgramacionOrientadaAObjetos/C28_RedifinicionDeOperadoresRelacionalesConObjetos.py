class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def __eq__(self,objeto2):
        if self.edad==objeto2.edad:
            return True
        else:
            return False

    def __ne__(self,objeto2):
        if self.edad!=objeto2.edad:
            return True
        else:
            return False

    def __gt__(self,objeto2):
        if self.edad>objeto2.edad:
            return True
        else:
            return False

    def __ge__(self,objeto2):
        if self.edad>=objeto2.edad:
            return True
        else:
            return False

#main
persona1=Persona('Juan',24)
persona2=Persona('Camilo',24)
if(persona1 == persona2):
    print("Las dos personas tienen la misma edad")
if(persona1 != persona2):
    print("Las dos personas difieren en edad")
if(persona1 > persona2):
    print("La persona 1 tiene mas edad que la persona 2")
if(persona1 >= persona2):
    print("La persona 1 tiene mas edad o igual que la persona 2")