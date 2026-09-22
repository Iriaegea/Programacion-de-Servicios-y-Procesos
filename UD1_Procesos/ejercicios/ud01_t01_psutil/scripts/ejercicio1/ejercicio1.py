# demostración de ejecución
import psutil

print(f"Hola mundo soy linux {psutil.LINUX}")
print(f"Hola mundo soy windows {psutil.WINDOWS}")


#plataforma sobre la que se ejecurta

if psutil.LINUX:
    print(f"Estás en LINUX")
elif psutil.WINDOWS:
    print(f"Estás en WINDOWS")
else:
    print(f"Estás en otro sistema operativo")



# información de CPUs
    # numero de CPUs
    print(f"El número de CPUs lógicas es {psutil.cpu_count()}")
    print(f"El número de CPUs físicas es {psutil.cpu_count(logical=False)}")

