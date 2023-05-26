H=int(input("Introduzca hora: "))
M=int(input("Introduzca minutos: "))
S=int(input("Introduzca segundos: "))
valido=False
if (H>0 and H<24)and(M>0 and M<60)and(S>0 and S<60):
    valido=True
if valido:
    print("Hora en formato correcto")
else:
    print("Hora invalida")