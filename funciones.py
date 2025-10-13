# Función: es un bloque de codigo que solo se ejecuta cuando lo llamamos. Permiten organizar y modularizar el codigo (reutilizacion)

def saludar(nombre, nacionalidad="Venezuela"):
    print("Hola", nombre, "de", nacionalidad)


nombre = "keyberth"
saludar(nombre)
saludar("Pedro", "España")


def sumar(a, b):
    return a + b


resultado = sumar(5, 3)
print(resultado)


def funcion():
    pass  # Placeholder para funciones vacias
