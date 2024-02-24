class Celular:                                          #clase
    def __init__(self, marca, modelo, camara):          #Funcion que se ejecuta automaticamente
        self.marca = marca                              #atributos dinamicos (dependen de los valores asignados al objeto)
        self.modelo = modelo                            #atributos dinamicos
        self.camara = camara                            #atributos dinamicos
        
    def llamar(self):
        return f"Estas haciendo una llamada desde un {self.marca}"
    
    def cortar(self):
        return f"Cortaste la llamada desde tu {self.modelo}"

celular1 = Celular("Samsung", "S23", "48MP")                #Objeto
celular2 = Celular("Apple", "Iphone 14 Pro Max", "48MP")    #Objeto

print(celular1.modelo)                                      #Ver el atributo del objeto
print(celular2.modelo)                                      #Ver el atributo del objeto

print(celular1.llamar())                                    #Ver el metodo del objeto
print(celular2.cortar())                                    #Ver el metodo del objeto