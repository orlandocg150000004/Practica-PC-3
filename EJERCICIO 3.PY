import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio**2

if __name__ == "__main__":
    # Ejemplo de uso
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio_circulo)
    area_circulo = circulo.calcular_area()
    print("El área del círculo es:", area_circulo)