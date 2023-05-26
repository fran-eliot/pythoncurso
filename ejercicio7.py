from datetime import datetime

fecha1=datetime.strptime(input("Introduzca fecha1 (dd-mm-yy):"),"%d/%m/%Y")
fecha2=datetime.strptime(input("Introduzca fecha2 (dd-mm-yy):"),"%d/%m/%Y")

diferencia=abs(fecha2-fecha1)

print("La cantidad de días de diferencia es: "+str(diferencia.days))