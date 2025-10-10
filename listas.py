# LISTAS: Las listas son ordenadas, modificables y permiten valores duplicados.

# frutas = ["manzana", "naranja", "kiwi", "pera", "uva", "naranja"]
# print(frutas)
# print(type(frutas))

# frutas[1] = "banana"
# print(frutas[1])

# lista = ["Keyberth", 5, True]

# print(lista)
# print(len(lista))
# print(len(frutas))

# print(frutas[0:2])

# if "manzana" in frutas:
#     print("La manzana está dentro de las frutas")

vehiculos = ["Auto", "Moto", "Avión"]

# Métodos
# Append (agregar un elemento al final de la lista)
vehiculos.append("Barco")
print(vehiculos)

# Insert (agregar un elemento en la posición que le indiquemos)
vehiculos.insert(1, "Bicicleta")
print(vehiculos)

# Remove (elimina el elemento que le indiquemos)
vehiculos.remove("Auto")
print(vehiculos)

# Pop (elimina el último elemento de la lista)
vehiculos.pop(1)
print(vehiculos)

# Sort (ordena la lista alfabéticamente)
vehiculos.sort()
print(vehiculos)

# Reverse (invierte el orden de la lista)
vehiculos.reverse()
print(vehiculos)

# Unir listas
coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion3 = coleccion1 + coleccion2
print(coleccion3)

coleccion1.extend(coleccion2)
print(coleccion1)
