USER="user"
PASS="pass"
login=False
contador=0
while contador<3 and not login:
    user=input("Introduzca usuario: ")
    pwd=input("Introduzca password: ")
    if (user==USER and pwd==PASS):
        login=True
    contador=contador+1
print("Login: "+str(login))