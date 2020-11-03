age=input("Introduce tu edad: ")

while age.isdigit()==False:
    print("No es una edad valida")

    age=input("Introduce tu edad: ")

if (int(age)<18):

    print("No puedes entrar")

elif (int(age)>=100):

    print("Demasiada edad me parece")

else:
    
    print("Tu edad es: ",age)

