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

# frecuencia de cada CPU
print(f"Frecuencias: {psutil.cpu_freq(percpu=True)}") 

# Uso de CPU por CPUs
print(f"Uso de cpu {psutil.cpu_percent(interval = 0.8, percpu = True)}")


#Información de memoria
#Memoria total
print(f"Memoria total:  {psutil.virtual_memory().total}")
#Meoria disponible
print(f"Memoria disponible:  {psutil.virtual_memory().available}")
#Porcentaje de memoria usada
print(f"Porcentaje de memoria usada:  {psutil.virtual_memory().percent}%")

#Información de discos
#Listado de particiones
print(f"Listado de particiones:  {psutil.disk_partitions(all=False)}")
#Uso de disco para cada unidad o partición
print(f"Uso de cada unidad/partición:  {psutil.disk_usage('/')}")
# 

#Número de operaciones de escritura

#Número de bytes leídos

#Número de bytes escritos