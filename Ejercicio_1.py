#Solicito los datos de entrada
name = input("Cual es el nombre del estudiante\n")
age = int(input("Cuál es la edad del estudiante:\n"))
course = input("Qué grado está cursando el estudiante:\n")
action = input("Qué deseas hacer:\n")


class Estudiante:
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado
        
    def estudiar(self):
        if action.lower() == "estudiar":
            print(f'el estudiante {self.Nombre} está estudiando')
        
student = Estudiante(name, age, course)

print(f"""
      DATOS DEL ESTUDIANTE: \n
      nombre: {name}
      edad: {age}
      grado: {course}
      
      """)

student.estudiar()