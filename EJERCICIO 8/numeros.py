import random

def generar_numeros():
    return [random.randint(0, 100) for _ in range(20)]

def mostrar_lista(lista):
    print("Lista obtenida:")
    for num in lista:
        print(num, end=" ")
    print()

def ordenar_y_mostrar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for num in lista_ordenada:
        print(num, end=" ")
    print()

if __name__ == "__main__":
    numeros = generar_numeros()
    mostrar_lista(numeros)
    ordenar_y_mostrar(numeros)
