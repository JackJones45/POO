class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")
        
class C(A):
    def hablar(self):
        print("Hola desde C")
        
class D(B,C):
    def hablar(self):
        print("Hola desde D")
        
objeto = D()

objeto.hablar()

print(D.mro())
