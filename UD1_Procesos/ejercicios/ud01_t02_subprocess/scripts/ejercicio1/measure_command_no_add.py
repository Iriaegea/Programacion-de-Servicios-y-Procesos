#ejemplo de uso: python measure_command.py python tarea.py ping as.com
#salida esperada
# Ejecutando: python tarea.py
# Salida del proceso:
# Tarea terminada

# Tiempo de ejecución: 2.01 segundos
# Código de salida: 0
import subprocess
import sys
import time

inicio = time.perf_counter()

argumentos = sys.argv[1:] #ignora la posicion 0 y pilla hasta el final


resultado = subprocess.run(argumentos, capture_output=True, text=True, shell=True) #shell es para que detecte q lo q meto es un comando

fin = time.perf_counter()

print(f"""
Ejecutando: {" ".join(argumentos)}
Salida del proceso:
{resultado.stdout}
{resultado.stderr}

Tarea terminada

Tiempo de ejecucion: {(fin-inicio):2.2f} segundos
Código de salida: {resultado.returncode}

""")
