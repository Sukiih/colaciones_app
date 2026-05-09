import json
import random

def ver_stock(stock):

    print("\nSTOCK DISPONIBLE")
    print("---------------------")

    for categoria, productos in stock.items():

        print("\n" + categoria.upper())

        for producto, cantidad in productos.items():
            print(producto + ":", cantidad)

def guardar_stock(stock):
    with open("stock.json", "w") as archivo:
        json.dump(stock, archivo, indent=4)


def agregar_stock(stock):

    categoria = input("Categoria: ").lower()
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))

    if categoria in stock:

        if producto in stock[categoria]:
            stock[categoria][producto] += cantidad

        else:
            stock[categoria][producto] = cantidad

        print("Producto agregado correctamente")
        guardar_stock(stock)
    else:
        print("La categoria no existe")
        


def quitar_stock(stock):

    categoria = input("Categoria: ").lower()
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))

    if categoria in stock:

        if producto in stock[categoria]:

            stock[categoria][producto] -= cantidad

            print("Producto descontado correctamente")
            guardar_stock(stock)

        else:
            print("El producto no existe")

    else:
        print("La categoria no existe")


def generar_colaciones(stock):

    #snacks = list(stock["snacks"].keys()) se reemplaza por lista para evitar usar algo sin stock
    snacks = []
    pesos_snacks = []
    for producto, cantidad in stock["snacks"].items():
        if cantidad > 0:
            snacks.append(producto)
            pesos_snacks.append(cantidad)
    #panes = list(stock["panes"].keys())
    panes = []
    pesos_panes = []
    for producto, cantidad in stock["panes"].items():
        if cantidad > 0:
            panes.append(producto)
            pesos_panes.append(cantidad)
    #bebidas = list(stock["bebidas"].keys())
    bebidas = []
    pesos_bebidas = []
    for producto, cantidad in stock["bebidas"].items():
        if cantidad > 0:
            bebidas.append(producto)
            pesos_bebidas.append(cantidad)
    #extras = list(stock["extras"].keys())
    extras = []
    pesos_extras = []
    for producto, cantidad in stock["extras"].items():
        if cantidad > 0:
            extras.append(producto)
            pesos_extras.append(cantidad)

    if len(snacks) == 0 or len(panes) == 0 or len(bebidas) == 0 or len(extras) == 0:
        print("No hay stock suficiente para generar una colacion")
        return

    snack = random.choices(
        snacks,
        weights=pesos_snacks,
        k=1
    )[0]

    pan = random.choices(
        panes,
        weights=pesos_panes,
        k=1
    )[0]

    bebida = random.choices(
        bebidas,
        weights=pesos_bebidas,
        k=1
    )[0]

    extra = random.choices(
        extras,
        weights=pesos_extras,
        k=1
    )[0]
    #descontamos stock

    stock["snacks"][snack] -= 1
    stock["panes"][pan] -= 1
    stock["bebidas"][bebida] -= 1
    stock["extras"][extra] -= 1

    guardar_stock(stock)

    return {
        "snack": snack,
        "pan": pan,
        "bebida": bebida,
        "extra": extra
    }

def generar_semana(stock):
    dias =[
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes"

    ]

    for dia in dias:
        colacion = generar_colaciones(stock)
        print("\n" + dia.upper())
        print("Snack:", colacion["snack"])
        print("Pan:", colacion["pan"])
        print("Bebida:", colacion["bebida"])
        print("Extra:", colacion["extra"])
    