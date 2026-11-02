#Ejercicio 6: Contador Seguro con Locks
#Crea un programa que utilice un multiprocessing.Lock para asegurar que varios procesos puedan incrementar un contador 
#compartido sin interferencias. Cada proceso debe incrementar el contador 100 veces. Al final, imprime el valor del contador.



import multiprocessing


def cosa1(contador, lock):
    for i in range(100):
        lock.acquire()
        contador.value +=  1
        lock.release



def cosa2(contador, lock):
    for i in range(100):
        lock.acquire()
        contador.value += 1
        lock.release



if __name__ == "__main__":

    contador = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()


    p1 = multiprocessing.Process(target=cosa1, args=(contador,lock))
    p2 = multiprocessing.Process(target=cosa2, args=(contador,lock))

    


    p1.start()
    p2.start()
    p1.join()
    p2.join()


    print("Contador final: {}".format(contador))