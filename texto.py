print("Hola 'mundo'")

ingles = "I'm Key"

multiples = """Hola
Mundo
desde 
las 
comillas
triples"""

print(ingles)
print(multiples)

palabra = "Murciélago"

print(len(palabra))

texto = "Este curso es de fundamentos de Python"

estaIncluida = "Python" in texto  # Esto es case sensitive
noEstaIncluida = "Javascript" not in texto

print(estaIncluida)
print(noEstaIncluida)

mayuscula = texto.upper()

print(mayuscula)

espacios = "     Este es el Texto       "
sinEspacios = espacios.strip()

print(sinEspacios)
