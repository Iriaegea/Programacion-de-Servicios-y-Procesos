import multiprocessing
import json

#pedidos = [] #cada proceso debe tener su propia copia, esto no sirve


def lector(fichero, diccionario_p):
    pedidos = []
    # global pedidos

    with open(fichero, "r", encoding="utf-8") as archivo:
        pedidos = json.load(archivo)
    for p in pedidos:
        diccionario_pedidos[p["id"]] = p

def procesador(diccionario_p):
    # global pedidos

    for k,p in diccionario_pedidos.items():
        p["importe_total"] = p["unidades"] * p["precio"]
        diccionario_pedidos[k] = p


if __name__ == "__main__":
    with multiprocessing.Manager as mp:
        diccionario_pedidos = mp.dict()

        p1 = multiprocessing.Process(
            target=lector,
            args=("pedidos.json", diccionario_pedidos)
        )

        p2 = multiprocessing.Process(
            target=procesador,
            args=(diccionario_pedidos,)
        )

        p1.start()
        p1.join()

        p2.start()
        p2.join()

        with open("pedidos_procesados.json", "w", encoding="utf-8") as archivo:
            json.dump(diccionario_pedidos.items(), archivo, indent=4, ensure_ascii=False)

        print("Procesamiento finalizado.")