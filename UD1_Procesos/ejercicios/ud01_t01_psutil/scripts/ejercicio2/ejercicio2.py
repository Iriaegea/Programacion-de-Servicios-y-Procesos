def mostrarServicios():
    


def mostrarServiciosFiltrados():



def mostrarDescripcionServicio():








if __name__ == "__main__":

opcion = 1

while opcion != 0:
    print(f"""MENU:
        1. Mostrar todos los servicios
        2. Mostrar servicios filtrados
        3. Mostrar descripción de un servicio
        0. SALIR""")

    opcion = int(input("selecciona una opcion: "))
    match opcion:
    case 1:
        mostrarServicios()
    case 2:
        mostrarServiciosFiltrados()
    case 3:
        mostrarDescripcionServicio()
    case 0: 
    print(f"Has salido del programa")
