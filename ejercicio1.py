variable='d'
a = int(input("Introduzca numero1:"))
b = int(input("Introduzca numero2:"))
c = int(input("Introduzca numero3:"))
menor = a
if (b<menor):
    menor=b
if (c<menor):
    menor=c
print("El menor es "+str(menor))