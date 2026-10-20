#Ejercicio 1: Memoria Compartida
#Crea un programa que utilice memoria compartida para que dos procesos puedan
#acceder y modificar una lista de números enteros. El primer proceso debe llenar 
#la lista con números del 1 al 10, y el segundo proceso debe multiplicar cada número 
#por 2.

import multiprocessing

def llenarLista(listaCompartida):
    for num in len(listaCompartida):
        listaCompartida[num]=num

    
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
    p1.join()

    p2.start()
    p2.join()


    print("Array visto desde el main después de los procesos: {}".format(listaCompartida[:]))
    




