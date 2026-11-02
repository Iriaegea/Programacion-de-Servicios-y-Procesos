#Ejercicio 3: Comunicación con multiprocessing.Queue
#Implementa un programa que utilice multiprocessing.
#Queue para que dos procesos se comuniquen. El primer 
#proceso debe generar una serie de números aleatorios 
#y enviarlos a través de la cola. El segundo proceso 
#debe recibir estos números y calcular su suma.

import multiprocessing

import time
import random

#rellena un array con numeros del 1 al 5 y lo mete en el qeue
def rellenar(miArray, q, cola_tiene_algo):
    for num in range(0,5):
        miArray[num] = num + 1 #(no es necesario el array , sobra, pero asi lo lleno)
        q.put(num+1)
        cola_tiene_algo.set()
        time.sleep(random.uniform(0,0.3))
    print("Mi array lleno: {}".format(list(miArray))) #hay q pasarlo a list pq no va



#pilla el qeue y  va sacando los numeros hasta vaciarlo para poder sumarlos
def sumar(q,cola_tiene_algo):
    suma = 0
    cola_tiene_algo.wait()
    while not q.empty():
        suma += q.get()
        print(suma)
        time.sleep(random.uniform(0,0.3))

    print("Resultado final: {}".format(suma))

if __name__ == '__main__':
    #crear array compartido
    miArray = multiprocessing.Array('i', 5)

    #crear el qeue
    q = multiprocessing.Queue()

    cola_tiene_algo = multiprocessing.Event()    
    
    proceso_rellenar = multiprocessing.Process(target=rellenar, args=(miArray, q, cola_tiene_algo))
    proceso_sumar = multiprocessing.Process(target=sumar, args=(q, cola_tiene_algo))


    proceso_rellenar.start()
    proceso_sumar.start()
    proceso_rellenar.join()
    proceso_sumar.join()
