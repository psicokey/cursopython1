x = 5
y = 7
z = 1

if x > y and x > z:
    print("x es mayor que y, y x es mayor que z")
elif x == y:
    print("x es igual a y")
else:
    print("Ninguna de las condiciones anteriores se cumplió")

a = "Python"
b = "Javascript"
c = "Python"

if a == c:
    if a == b:
        print("a es igual a b pero distinto de c")
    else:
        print("estoy saliendo por el else del if interno")
else:
    print("a no es igual a c")

e = 10
f = 10

if e == f:
    pass  # para ignorar la estructura if hasta tanto definamos que comportamiento se espera
