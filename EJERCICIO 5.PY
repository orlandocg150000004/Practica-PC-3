class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print("Nombre:", self.nombre)
        print("Número de registro:", self.numero_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", self.notas)
    
    def set_edad(self, edad):
        self.edad = edad
    
    def set_notas(self, notas):
        self.notas = notas

if __name__ == "__main__":
    # Ejemplo de uso
    nombre_alumno = input("Ingrese el nombre del alumno: ")
    numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
    alumno = Alumno(nombre_alumno, numero_registro_alumno)

    # Establecer la edad del alumno
    edad_alumno = int(input("Ingrese la edad del alumno: "))
    alumno.set_edad(edad_alumno)

    # Establecer las notas del alumno
    notas_alumno = input("Ingrese las notas del alumno separadas por comas: ").split(',')
    alumno.set_notas(notas_alumno)

    # Mostrar información del alumno
    alumno.display()