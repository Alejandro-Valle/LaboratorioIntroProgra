#LS13_GAVB1000623

cantidad=True
while cantidad==True:
    cantidad_circulos= int(input("Ingrese el número de circulos que quiere: "))
    if cantidad_circulos<0:
        print("Debe de ingresar un número positivo. ")
    else:
        cantidad=False

class circulo:
    def __init__(self, radio):
        self.radio=radio
    
    def obtenerperimetro(self):
        return 2*self.radio*3.1416
    
    def obtenerarea(self):
        return 3.1416*self.radio*self.radio

    def obtenervolumen(self):
        return (4*3.1416*self.radio*self.radio*self.radio)/3


for x in range(cantidad_circulos):

    ciclo=True

    while ciclo==True:

        radio=float(input("Ingrese el radio del circulo"+" "+ str(x+1)+": "))

        if radio<0:
            print("No se pueden tener medidas negativas")
        else:
            circulo1=circulo(radio)
            print("_____CARACTERISTICAS DEL CIRCULO" +" " +str(x+1)+"_____")
            print("El área del circulo es: ")
            print(circulo1.obtenerarea())
            print("El perimetro del círculo es: ")
            print(circulo1.obtenerperimetro())
            print("El volumen del círculo es: ")
            print(circulo1.obtenervolumen())
            ciclo=False



    