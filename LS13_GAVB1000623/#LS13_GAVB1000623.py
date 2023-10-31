#LS13_GAVB1000623

class circulo:
    def __init__(self, radio):
        self.radio=radio
    
    def obtenerperimetro(self):
        return 2*self.radio*3.1416
    
    def obtenerarea(self):
        return 3.1416*self.radio*self.radio

    def obtenervolumen(self):
        return (4*3.1416*self.radio*self.radio*self.radio)/3

ciclo=True

while ciclo==True:

    radio=float(input("Ingrese el radio del circulo: "))

    if radio<0:
        print("No se pueden tener medidas negativas")
    else:
        circulo1=circulo(radio)
        print("_____CARACTERISTICAS DEL CIRCULO_____")
        print("El área del circulo es: ")
        print(circulo1.obtenerarea())
        print("El perimetro del círculo es: ")
        print(circulo1.obtenerperimetro())
        print("El volumen del círculo es: ")
        print(circulo1.obtenervolumen())
        ciclo=False



    