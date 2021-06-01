numeros = [3, 5, 25, 33, 45, 97, 107]

# def multiplos(num):
#     if num %5 == 0:
#         print("Es multiplo de 5")
#     else:
#         print("No es multiplo de 5")

print(list(filter(lambda num: num%5==0, numeros)))

