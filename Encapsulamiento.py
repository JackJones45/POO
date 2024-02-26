class MiClase:
    def __init__(self):
        self._atribito_privado = "Valor"       #atributo privado         
        #La forma de decir en python que el atributo es privado es con el guion bajo (igualmente puede acceder)
        self.__atributo_muy_privado = "Valor muy privado"   #Atributo muy privado
        #La forma de decir en python que el atributo es muy privado es con doble guion bajo (no se puede acceder facilmente)
    
    def __hablar(self):
        print("Hola, soy un metodo privado")
        
objeto = MiClase()

# print(objeto._atribito_privado)
print(objeto._atribito_muy_privado)