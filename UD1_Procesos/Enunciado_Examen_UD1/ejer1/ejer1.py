import multiprocessing

def lector(fichero_entrada, cola): #add cola
    """
    Lee el fichero de entrada y devuelve una lista
    con los números correspondientes a cada línea.
    """

    # datos = []

    with open(fichero_entrada, "r") as fichero:
        for linea in fichero:
            numeros = [int(n) for n in linea.split()]

            if numeros == [0]:
                cola.put(0) #add
                break

            # datos.append(numeros)
            cola.put(numeros) #add

    return datos


def cifrador(cola, fichero_salida): #cambiar datos por cola
    """
    Calcula la clave de cada línea, cifra los códigos
    ASCII y escribe los resultados en el fichero de salida.
    """

    with open(fichero_salida, "w") as fichero:

        # for numeros in datos:
        while True:
            numeros = cola.get()

            if numeros.isEmpty

            # Calcula la clave de cifrado
            clave = int(sum(numeros) / len(numeros)) % 26

            cifrados = []

            for codigo in numeros:

                # Letras mayúsculas
                if 65 <= codigo <= 90:
                    cifrado = 65 + (codigo - 65 + clave) % 26

                # Letras minúsculas
                elif 97 <= codigo <= 122:
                    cifrado = 97 + (codigo - 97 + clave) % 26

                # Otros caracteres sin modificar
                else:
                    cifrado = codigo

                cifrados.append(cifrado)

            # Inserta la clave al principio del resultado
            resultado = [clave] + cifrados

            # Escribe los números separados por espacios
            fichero.write(" ".join(map(str, resultado)) + "\n")


if __name__ == "__main__":

    fichero_entrada = "entrada.txt"
    fichero_salida = "salida.txt"

    # datos = lector(fichero_entrada)

    # cifrador(datos, fichero_salida)

    cola_datos = multiprocessing.Queue() #add

    proceso_lector = multiprocessing.Process(target=lector, args=(fichero_entrada, cola_datos))#add
    
    proceso_cifrador = multiprocessing.Process(target = cifrador, args=(cola_datos, fichero_salida))#add


    #las colas son seguras, me viene mejor que usar array o diccionario pq entonces tenfria q sincronizarlos
    proceso_lector.start()
    proceso_cifrador.start()
    proceso_lector.join()
    proceso_cifrador.join()
    print("Procesamiento finalizado.")