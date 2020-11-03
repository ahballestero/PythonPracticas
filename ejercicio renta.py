print("Tipo impositivo declaración renta")

renta=float(input("Introduce tu renta: "))

tipoimp=0

if renta <12000:
    tipoimp=+7
    print(f"A la renta {renta}, le corresponde un {tipoimp}% impositivo")
elif renta >=12000 and renta <=18000:
    tipoimp=+15
    print(f"A la renta {renta}, le corresponde un {tipoimp}% impositivo")
elif renta >18000 and renta <=35000:
    tipoimp=+21
    print(f"A la renta {renta}, le corresponde un {tipoimp}% impositivo")
elif renta >35000 and renta <=70000:
    tipoimp=+35
    print(f"A la renta {renta}, le corresponde un {tipoimp}% impositivo")
else:
    tipoimp=+45
    print(f"A la renta {renta}, le corresponde un {tipoimp}% impositivo")

