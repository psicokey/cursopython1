try:
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")


try:
    print(x)
except NameError:
    print("La variable x no está definida")
finally:
    print("Esto será ejecutado siendo exitoso o no el bloque")

try:
    numero = 10
    if numero > 5:
        print("Numero es mayor que 5")
except SyntaxError:
    print("Necesitamos poner ':' al usar if")
