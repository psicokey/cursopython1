# Conjunto (set): Colección no ordenada de elementos únicos (no se puede acceder por índice)

frutas = {"manzana", "naranja", "kiwi", "pera", "uva", "naranja"}
print(frutas)
print(type(frutas))
print(len(frutas))

print("manzana" in frutas)
print("pera" in frutas)

# Agregar elementos
# add
frutas.add("banana")
print(frutas)

# Update (agrega varios elementos)
frutasTropicales = {"mandarina", "coco", "sandía"}
frutas.update(frutasTropicales)  # Agregar listas, tuplas o conjuntos
print(frutas)

# Eliminar elementos
# remove (si el elemento no existe, lanza un error)
frutas.remove("mandarina")
print(frutas)
# discard (si el elemento no existe, no lanza error)
frutas.discard("pera")
print(frutas)
# pop (elimina un elemento aleatorio)
frutas.pop()
print(frutas)
# clear (elimina todos los elementos)
frutas.clear()
print(frutas)

# conjuntos = {"Keyberth", 5, True}
# print(conjuntos)
# print(type(conjuntos))

# for item in conjuntos:
#     print(item)

print("----------------------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}
c = a.union(b)  # une dos conjuntos
print(c)

i = a.intersection(b)  # elementos en común entre dos conjuntos
print(i)

d = a.difference(b)  # elementos en a que no están en b
print(d)
