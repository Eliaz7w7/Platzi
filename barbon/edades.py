nombre1 = input("Ingrese el nombre de la primera persona: ")
edad1 = int(input("Ingrese la edad de la primera persona: "))
nombre2 = input("ingrese el nombre de la persona")
edad2 = int(input("Ingrese la edad de la persona"))

if edad1 > edad2:
    print(nombre1+" tiene "+str(edad1)+" es el mayor")
elif edad2 > edad1:
    print(nombre2+" tiene "+str(edad2)+" es el mayor")
else:
    print(nombre1+" y "+nombre2+" tienen la misma edad")
