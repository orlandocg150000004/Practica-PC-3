import operaciones

if __name__ == "__main__":
    # Ejemplos de uso
    print("Suma:", operaciones.suma(5, 3))
    print("Resta:", operaciones.resta(10, 4))
    print("Producto:", operaciones.producto(6, 7))
    print("División:", operaciones.division(8, 2))
    # Ejemplos de errores
    print("Intento de división por cero:", operaciones.division(10, 0))
    print("Operación inválida:", operaciones.suma("a", 3))