from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial


def main():
    while True:
        # mostrar el menu del café
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            # Pedir un café
            pedir_cafe()
        elif opcion == '2':
            # Ver el historial
            ver_historial()
        elif opcion == '3':
            print("\n Gracias por usar el sistema de pedidos de café. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
