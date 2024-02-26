#Parte 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def info_persona(self):
        return f"mi nombre es {self.nombre} y mi edad es {self.edad}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def grado_estudio(self):
        return f"El estudiante {self.nombre} está cursando el grado {self.grado}"

April = Estudiante("April", 32, "decimo")

print(April.grado_estudio())


#Parte 2

class Animal:
    def comer(self):
        return "El animal esta comiendo"

class Mamifero(Animal):
    def amamantar(self):
        return "Este animal se amamanta"

class Ave(Animal):
    def volar(self):
        return "Este animal vuela"

class Murcielago(Mamifero, Ave):
    pass

bat = Murcielago()
aguila = Ave()
print(bat.volar())
print(bat.comer())
print(bat.amamantar())
print(aguila.volar())