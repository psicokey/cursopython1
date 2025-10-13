# Lambda: es una funcion pequeña y anomima que puede tener muchos argumentos pero solo una expresion.

# Sintaxis: lambda argumentos: expresion

# x = lambda a: a + 10
# print(x(5))

# y = lambda a, b: a + b
# print(y(2, 3)) # 5

def mifuncion(n):
    return lambda a: a * n


duplicador = mifuncion(2)
triplicador = mifuncion(3)
quintuplicador = mifuncion(5)

print(duplicador(5))  # 10
print(triplicador(5))  # 15
print(quintuplicador(5))  # 25
