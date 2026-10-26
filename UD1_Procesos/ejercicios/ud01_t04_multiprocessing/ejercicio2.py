#Ejercicio 2: Clase Manager
#Desarrolla un programa que utilice la 
#clase Manager para compartir un diccionario entre varios 
#procesos. Cada proceso debe agregar una clave única al 
#diccionario con un valor aleatorio. Al final, imprime el diccionario completo.


import multiprocessing
import random


# asiga el primer valor al diccionario compartido
def valor1(diccionario):
    diccionario[1]= random.random()

# asigna el siguiente valor al diccionario
def valor2(diccionario):
    diccionario[2] = random.random()


if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        diccionario = manager.dict()

        p1 = multiprocessing.Process(target=valor1, args=(diccionario,) )
        p2 = multiprocessing.Process(target=valor2, args=(diccionario,) )

        p1.start()
        p1.join()
        p2.start()
        p2.join()

        print(diccionario)
