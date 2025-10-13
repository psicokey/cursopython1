# Coleccion de pares clave-valor

auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020
}

print(auto)
print(type(auto))
print(auto["marca"])
print(auto.get("modelo"))

print(auto.keys())
print(auto.values())

if "marca" in auto:
    print("Marca es una de las propiedades de estes diccionario")

auto["año"] = 2025
print(auto["año"])

auto["color"] = "Rojo"
print(auto)

auto.update({"año": 2022})
auto.update({"puertas": 4, "transmision": "Automática"})
print(auto)

# auto.pop("puertas")
auto.pop("transmision")
# print(auto)

# auto.popitem()
# print(auto)

# auto.clear()
# print(auto)

for k in auto:
    print(k)
print("--------------")
for v in auto.values():
    print(v)
print("--------------")
for k, v in auto.items():
    print(k, v)

# Diccionarios anidados

familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 6
    }
}

print(familia["hijo1"]["nombre"])
