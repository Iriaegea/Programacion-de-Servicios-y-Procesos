# demostración de ejecución
import psutil
from datetime import datetime


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
# Número de operaciones de lectura
print(f"Múmero de operaciones de lectura: {psutil.disk_io_counters(perdisk=False, nowrap=True).read_count}")


#Número de operaciones de escritura
print(f"Múmero de operaciones de escritura: {psutil.disk_io_counters(perdisk=False, nowrap=True).write_count}")

#Número de bytes leídos

print(f"Múmero de bytes leidos: {psutil.disk_io_counters(perdisk=False, nowrap=True).read_bytes}")
#Número de bytes escritos
print(f"Múmero de bytes escritos: {psutil.disk_io_counters(perdisk=False, nowrap=True).write_bytes}")


#Estadísticas de red
#bytes enviados
print(f"BYTES ENVIADOS: {psutil.net_io_counters(pernic=False, nowrap=True).bytes_sent}")

#bytes recibidos
print(f"BYTES RECIBIDOS: {psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv}")

#paquetes enviados
print(f"PAQUETES ENVIADOS: {psutil.net_io_counters(pernic=False, nowrap=True).packets_sent}")

#paquetes recibidos
print(f"PAQUETES ENVIADOS: {psutil.net_io_counters(pernic=False, nowrap=True).packets_recv}")



#Guardar información del sistema:
#Realizará un volcado de la información del sistema 
#que se muestra por pantalla a un fichero JSON en la 
#ruta que se proporcione, siendo el nombre del fichero 
#el siguiente: yyyyMMddhhmmss-system-info.json

fechaactual = datetime.datetime.now()
fechaactualformateada = fechaactual.strftime("%Y%m%d%H%M%S")
archivo = fr'D:\iriae\Desktop\PSP\UD1_Procesos\ejercicios\ud01_t01_psutil\scripts\ejercicio2\{fechaactualformateada}-system-info.json'


with open(archivo, mode = "w") as file:
    json.dump()