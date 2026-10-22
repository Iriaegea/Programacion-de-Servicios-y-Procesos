#Ejercicio 1: Memoria Compartida
#Crea un programa que utilice memoria compartida para que dos procesos puedan
#acceder y modificar una lista de números enteros. El primer proceso debe llenar 
#la lista con números del 1 al 10, y el segundo proceso debe multiplicar cada número 
#por 2.

import multiprocessing
import time
import random

def llenarLista(listaCompartida):
    for num in range(0,10):
        listaCompartida[num]=num +1
        time.sleep(random.random())
    
    print("Resultado de llenar la lista: {}".format(listaCompartida[:]))


def dobleLista(listaCompartida):
    for index, num in enumerate(listaCompartida):
        listaCompartida[index] = (index +1) *2

    print("Resultado doble de la lista: {}".format(listaCompartida[:]))



if __name__ == "__main__":
   

    listaCompartida = multiprocessing.Array('i', 10)
    
    p1 = multiprocessing.Process(target=llenarLista, args=(listaCompartida,))
    p2 = multiprocessing.Process(target=dobleLista, args=(listaCompartida,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    


    print("Array visto desde el main después de los procesos: {}".format(listaCompartida[:]))
    




