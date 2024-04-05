def obtener_calificaciones():
    while True:
        try:
            # Solicitar al usuario la lista de calificaciones separadas por comas
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            
            # Dividir la cadena en calificaciones individuales y almacenarlas en una lista
            calificaciones_lista = calificaciones_str.split(',')
            
            # Convertir cada calificación en un entero
            calificaciones_entero = [int(calificacion.strip()) for calificacion in calificaciones_lista]
            
            return calificaciones_entero
        except ValueError:
            print("Error: Las calificaciones deben ser números enteros.")
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    calificaciones = obtener_calificaciones()
    print("Calificaciones ingresadas:", calificaciones)