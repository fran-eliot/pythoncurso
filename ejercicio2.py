frase=input("introduzca una frase: ")
letra=input("introduzca una letra: ")
contador = 0
for i in frase:
    if i==letra:
        contador=contador+1
print("La frase tiene "+str(contador)+" veces la letra "+letra)