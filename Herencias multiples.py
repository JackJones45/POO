class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return "Hola, estoy hablando"
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        return f"mi habilidad es {self.habilidad}"
        
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)  #Hacemos referencia directa de la clase padre que estamos heredando los atributos
        Artista.__init__(self, habilidad)                   #Hacemos referencia directa de la clase padre que estamos heredando los atributos
        self.salario = salario                              #Atributo propio de la clase hija
        self.empresa = empresa
        
    def mensaje(self):
        return f"Hola mi nombre es {self.nombre}, {super().mostrar_habilidad()} y trabajo en {self.empresa}"
#La palabra reservada super aplica solo para los metodos que tienen las clases padres, para los atributos usamos el self    

April = EmpleadoArtista("April", 32, "Canadiense", "Cocinar rico", "100000CAD", "Hamilton Hospital")

print(April.mensaje())
print(April.salario)
print(April.edad)


#Para validar si las clases son herencias de otras clases o si los objetos son instancias de alguna clase
herencia = issubclass(EmpleadoArtista, Artista)
print(herencia)
instancia = isinstance(April, Artista)
print(instancia)
