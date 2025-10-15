
# open(nombre, modo)

# R (read) - Lectura
# W (write) - Escritura
# X (create) - Crear

try:
    # f = open("archivo.txt", "r")
    # print(f.readline())
    # f.close()
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open("archivo.txt", "x")
    print("El archivo no existe")


try:
    with open("archivo.txt", "a") as f:  # a añade contenido al final del archivo
        f.write("\n")
        f.write("Hola mundo desde Write en el with")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")

# try:
#     with open("archivo.txt", "w") as f:  # W sobreescribe el archivo
#         f.write("Hola mundo desde Write en el with")
#     with open("archivo.txt", "r", encoding="utf-8") as f:
#         print(f.readline())
# except FileNotFoundError:
#     print("El archivo no existe")
