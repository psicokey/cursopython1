# Tupla: Coleccion ordenada e inmutable de elementos que permiten duplicados

tecnologias = ("Python", "JavaScript", "Go", "Python")
print(tecnologias)
print(type(tecnologias))
print(tecnologias[1])

print(len(tecnologias))

fruta = ("manzana",)
print(type(fruta))

tupla = ("Keyberth", 5, True)
print(tupla)

x, y, z = tupla
print(x)
print(y)
print(z)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)

print(tupla * 2)

for item in tupla:
    print(item)

print("---------------------------")

tuplaAModificar = ("Python", "Javascript", "Go")
listaComodin = list(tuplaAModificar)
# print(listaComodin)
listaComodin.append("React")
tuplaAModificar = tuple(listaComodin)

print(tuplaAModificar)
