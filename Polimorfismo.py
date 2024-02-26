class Gato:
    def sonido(self):
        return "Miau"
    
class Perro:
    def sonido(self):
        return "Guau"
    
gato = Gato()
perro = Perro()

print(gato.sonido())        #Polimorfismo de funcion
print(perro.sonido())       #Polimorfismo de funcion
#Acá hay polimorfismo ya que el mensaje es el mismo, solo cambia el objeto al que se lo envio

#Otra forma de hacer polimorfismo
def hacer_sonido(Animal):
    print(Animal.sonido())
    
hacer_sonido(gato)          #Polimorfismo de parametro
hacer_sonido(perro)         #Polimorfismo de parametro