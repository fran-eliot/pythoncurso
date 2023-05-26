a = int(input("Introduzca el numero 1: "))
b = int(input("Introduzca el numero 2: "))
operacion = input ("Introduzca operacion: suma(s)/resta(r): ")
resu = 0
if operacion=="s":
    resu = a + b
if operacion=="r":
    resu = a - b
print("El resultado es "+str(resu))