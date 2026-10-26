#Ejercicio 4: Comunicación con multiprocessing.Pipe
#Escribe un programa que utilice multiprocessing.
#Pipe para la comunicación entre dos procesos. 
#El primer proceso debe enviar una cadena de texto a través 
#del tubo, y el segundo proceso debe recibirla y convertirla 
#a mayúsculas antes de imprimirla.


import multiprocessing 

def enviarCdena(conn, cadena):
    conn.send(cadena)
    print("Enviada la cadena: {}".format(cadena))
    conn.close()

def mayusculizar(conn):
    cadena = conn.recv()
    print("El mensaje en mayúsculas es: {}".format(cadena.upper()))
    #no hace falta cerrarlo pq ya se queda sin mensajes

if __name__ == '__main__':
    cadena = "hola"


    
    parent_conn, child_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=enviarCdena, args=(parent_conn, cadena))
    p2 = multiprocessing.Process(target= mayusculizar, args=(child_conn,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()