from geometria import Circulo, Rectangulo, Cuadrado

def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    area = circulo.calcular_area()
    print("El área del círculo es:", area)

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo, ancho)
    area = rectangulo.calcular_area()
    print("El área del rectángulo es:", area)

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = Cuadrado(lado)
    area = cuadrado.calcular_area()
    print("El área del cuadrado es:", area)

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            calcular_area_circulo()
        elif opcion == "2":
            calcular_area_rectangulo()
        elif opcion == "3":
            calcular_area_cuadrado()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")