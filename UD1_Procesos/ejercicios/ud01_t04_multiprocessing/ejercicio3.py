#Ejercicio 3: Comunicación con multiprocessing.Queue
#Implementa un programa que utilice multiprocessing.
#Queue para que dos procesos se comuniquen. El primer 
#proceso debe generar una serie de números aleatorios 
#y enviarlos a través de la cola. El segundo proceso 
#debe recibir estos números y calcular su suma.

import multiprocessing

def rellenar(miArray, q):
    for num in range(0,4):
        miArray[num] = num + 1
        q.put(num+1)




def sumar(q):
    suma = 0
    while not q.empty():
        suma += q.get()

print(suma)

if __name__ == '__main__':

    miArray = multiprocessing.Array('i', 5)
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=rellenar, args=(miArray, q))
    p2 = multiprocessing.Process(target=sumar, args=(q))


    p1.start()
    p1.join()

    p2.start()
    p2.join()
