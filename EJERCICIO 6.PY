class Producto:
    def __init__(self, nombre, precio, año_fabricacion):
        self.nombre = nombre
        self.precio = precio
        self.año_fabricacion = año_fabricacion

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Año de fabricación: {self.año_fabricacion}"


class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el catálogo.")
        else:
            print("Productos en el catálogo:")
            for producto in self.productos:
                print(producto)

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año_fabricacion == año]
        if productos_filtrados:
            print(f"Productos fabricados en el año {año}:")
            for producto in productos_filtrados:
                print(producto)
        else:
            print(f"No hay productos fabricados en el año {año} en el catálogo.")


if __name__ == "__main__":
    # Ejemplo de uso
    catalogo = Catalogo()

    # Agregar algunos productos al catálogo
    catalogo.agregar_producto(Producto("Llantas", 150, 2022))
    catalogo.agregar_producto(Producto("Filtro de aceite", 20, 2021))
    catalogo.agregar_producto(Producto("Batería", 100, 2023))

    # Mostrar todos los productos en el catálogo
    catalogo.mostrar_productos()

    # Filtrar productos por año de fabricación
    catalogo.filtrar_por_año(2022)