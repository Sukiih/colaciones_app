import json

from funciones import ver_stock
from funciones import agregar_stock
from funciones import quitar_stock
from funciones import generar_colaciones
from funciones import generar_semana


with open("stock.json", "r") as archivo:
    stock = json.load(archivo)


print("\n===== MENU =====")
print("1. Ver stock")
print("2. Agregar stock")
print("3. Quitar stock")
print("4. Generar colaciones")
print("5. Salir")


opcion = input("\nSelecciona una opcion: ")


if opcion == "1":
    ver_stock(stock)

elif opcion == "2":
    agregar_stock(stock)

elif opcion == "3":
    quitar_stock(stock)

elif opcion == "4":
    generar_semana(stock)

elif opcion == "5":
    print("Adios")

else:
    print("Opcion invalida")