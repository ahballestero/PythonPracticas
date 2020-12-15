import queue

cola1=queue.PriorityQueue()

cola1.put((3,"Madrid"))
cola1.put((1,"Bogota"))
cola1.put((2,"Mexico DF"))

print(cola1.get())


while not cola1.empty():
    print(cola1.get())

if cola1.empty():
    print("La cola está vacía")

    