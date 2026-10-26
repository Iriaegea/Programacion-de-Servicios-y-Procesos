#Ejercicio 3: Comunicación con multiprocessing.Queue
#Implementa un programa que utilice multiprocessing.
#Queue para que dos procesos se comuniquen. El primer 
#proceso debe generar una serie de números aleatorios 
#y enviarlos a través de la cola. El segundo proceso 
#debe recibir estos números y calcular su suma.

import multiprocessing

#rellena un array con numeros del 1 al 5 y lo mete en el qeue
def rellenar(miArray, q):
    for num in range(0,5):
        miArray[num] = num + 1 #(no es necesario el array , sobra, pero asi lo lleno)
        q.put(num+1)
    print("Mi array lleno: {}".format(list(miArray))) #hay q pasarlo a list pq no va



#pilla el qeue y hasta q va sacando los numeros hasta vaciarlo para poder sumarlos
def sumar(q):
    suma = 0
    while not q.empty():
        suma += q.get()
        print(suma)

    print("Resultado final: {}".format(suma))

if __name__ == '__main__':
    #crear array compartido
    miArray = multiprocessing.Array('i', 5)

    #crear el qeue
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=rellenar, args=(miArray, q))
    p2 = multiprocessing.Process(target=sumar, args=(q, ))


    p1.start()
    p1.join()

    p2.start()
    p2.join()
