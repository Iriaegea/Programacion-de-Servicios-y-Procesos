import psutil

def mostrarMenu():
    print(f"""MENU:
        1. Mostrar info de todos los procesos.
        2. Filtrar procesos por uso de memoria.
        3. Filtrar procesos por uso de CPU.
        4. Mostrar árbol de procesos.
        0. SALIR""")
    return int(input("selecciona una opcion: "))


def mostrarInfoProcesos():
    #array por compresión
    arrayProcesos = [p for p in psutil.process_iter(attrs = ['pid', 'name', 'username'])]
    for p in arrayProcesos : 
        print(f"pid: {p.pid}, name: {p.name}, username: {p.username}\n")
        


def porUsoDeMemoria(usoMemoria):
    procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username']) if p.memory_percent() >usoMemoria]
    procesos.sort(key=lambda p: p.memory_percent(), reverse = True)
    for p in procesos:
        print(f"pid: {p.pid}, name: {p.name}, username: {p.username}\n")

    print(procesos)


def porUsoDeCpu(usoCpu):
    procesos = [p for p in psutil.process_iter(attrs=['pid', 'name', 'username','memory_info']) if p.cpu_percent(interval=0.5)>usoCpu]

    procesos.sort(key=lambda p: p.cpu_percent(interval=0.5))

    print(procesos)


#def mostrarArbol():


if __name__ == "__main__":

    opcion = 1

    while opcion != 0:
        opcion = mostrarMenu()

    
        match opcion:
            case 1:
               mostrarInfoProcesos()
            case 2:
                usoMemoria = input("¿Por encima de qué porcentaje de uso de memoria? : ")
                porUsoDeMemoria(usoMemoria)

            case 3:
                usoCpu= input("Por")
                porUsoDeCpu()
            case 4: 
                mostrarArbol()
            case 0: 

                print(f"Has salido del programa")
            case _:
                print(f"Opción no válida")

    
