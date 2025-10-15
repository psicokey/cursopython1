ARCHIVO_PEDIDOS = "pedidos.txt"


def pedir_cafe():
    print("Elige el café que prefieras: ")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Americano")

    opcion = input("Selecciona una opción (1-4): ")

    cafes = {
        "1": "Espresso",
        "2": "Latte",
        "3": "Cappuccino",
        "4": "Americano"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print("Has pedido un café: " + cafe_elegido + ". Preparando tu café...!")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("La opcion no es válida por favor intenta de nuevo")
