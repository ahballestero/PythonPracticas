def decoration(funcion):
  def funcion_interna():
    print ("A continuacion vamos a ejecutar una funcion pedorra")
    funcion()
    print("Ya hemos terminado")
  return funcion_interna





@decoration
def suma():
  print(50+30)


@decoration
def resta():
  print(75-65)


suma()

resta()
