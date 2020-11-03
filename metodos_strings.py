age=input("Introduce tu edad: ")

while age.isdigit()==False:
    print("No es una edad valida")

    age=input("Introduce tu edad: ")

if (int(age)<18):

    print("No puedes entrar")
else:
    
    print("Tu edad es: ",age)

