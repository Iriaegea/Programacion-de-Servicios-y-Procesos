import psutil

# numero de CPUs
print(f"El número de CPUs lógicas es {psutil.cpu_count()}")
cpuslogicas = psutil.cpu_count()
print(f"El número de CPUs físicas es {psutil.cpu_count(logical=False)}")
cpusfisicas = psutil.cpu_count(logical=False)
