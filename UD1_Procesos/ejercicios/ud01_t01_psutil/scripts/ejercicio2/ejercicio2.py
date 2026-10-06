import psutil

def mostrarServicios():
    
    for s in psutil.win_service_iter():
        print(f"{s.name()}: ({s.pid()}, {s.status()}, {s.start_type()})")

def mostrarServiciosFiltrados():
    filtro = set(input("Filtra: ").split())
    for s in psutil.win_service_iter():
        if filtro.issubset(set([s.status(), s.start_type()])):
            print(f"{s.name()}: ({s.pid()}, {s.status()}, {s.start_type()})")


def mostrarDescripcionServicio():
    nombreServicio = input(f"Escribe el nombre del servicio que quieres buscar: ")
    for s in psutil.win_service_iter():
        if(s.name() == nombreServicio):
            print(f"Descripción: {s.description()}")

        
    
    

def mostrarMenu():
    print(f"""MENU:
        1. Mostrar todos los servicios
        2. Mostrar servicios filtrados
        3. Mostrar descripción de un servicio
        0. SALIR""")
    return int(input("selecciona una opcion: "))



if __name__ == "__main__":

    opcion = 1

    while opcion != 0:
        opcion = mostrarMenu()

    
        match opcion:
            case 1:
                mostrarServicios()

            case 2:
                mostrarServiciosFiltrados()

            case 3:

                mostrarDescripcionServicio()

            case 0: 

                print(f"Has salido del programa")
            case _:
                print(f"Opción no válida")

    
