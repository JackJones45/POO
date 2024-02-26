class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return f"Hola, {self.nombre} está hablando"
        
class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):   #Metodo constructor para todos los atributos de la clase
        super().__init__(nombre, edad, nacionalidad)    #acá definimos que atributos vienen de la clase padre
        self.trabajo = trabajo                          #Atributos propios de la clase hija
        self.salario = salario

April = Empleado("April", 32, "Canadiense", "Enfermera", "100000CAD")

April.hablar()

print(April.nacionalidad)
print(April.trabajo)
print(April.hablar())