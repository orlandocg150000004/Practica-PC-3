def obtener_porcentaje(fraction):
    try:
        # Dividir la fracción en X y Y
        x, y = map(int, fraction.split('/'))

        # Verificar si X/Y es menor al 1%
        if x / y < 0.01:
            return 'E'
        # Verificar si X/Y es mayor al 99%
        elif x / y > 0.99:
            return 'F'
        # En otro caso, devolver el valor en porcentaje
        else:
            return str(round(x / y * 100)) + '%'
    except ValueError:
        return "Error: La fracción debe tener el formato X/Y y ambos deben ser números enteros."
    except ZeroDivisionError:
        return "Error: El denominador no puede ser cero."
    except Exception as e:
        return "Error:", e

if __name__ == '__main__':
    while True:
        fraction = input("Ingrese una fracción en formato X/Y: ")
        result = obtener_porcentaje(fraction)
        print("Cantidad de combustible en el tanque:", result)
        if result not in ['E', 'F']:
            break