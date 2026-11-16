import multiprocessing
import json

pedidos = []


def lector(fichero):
    global pedidos

    with open(fichero, "r", encoding="utf-8") as archivo:
        pedidos = json.load(archivo)


def procesador():
    global pedidos

    for pedido in pedidos:
        pedido["importe_total"] = pedido["unidades"] * pedido["precio"]


if __name__ == "__main__":

    p1 = multiprocessing.Process(
        target=lector,
        args=("pedidos.json",)
    )

    p2 = multiprocessing.Process(
        target=procesador
    )

    p1.start()
    p1.join()

    p2.start()
    p2.join()

    with open("pedidos_procesados.json", "w", encoding="utf-8") as archivo:
        json.dump(pedidos, archivo, indent=4, ensure_ascii=False)

    print("Procesamiento finalizado.")