class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

if __name__ == "__main__":
    # Ejemplo de uso
    largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
    ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = Rectangulo(largo_rectangulo, ancho_rectangulo)
    area_rectangulo = rectangulo.calcular_area()
    print("El área del rectángulo es:", area_rectangulo)