
# LS12_GAVB1000623

class calculadora:
    def __init__(self):
        self.numero1=0.0
        self.numero2=0.0

    def obtenernumero1(self, numero):
        self.numero1= numero
    
    def obtenernumero2(self, numero):
        self.numero2=numero

    def ingresarnumero1(self, numero1):
        self.numero1= numero1

    def ingresarnumero2(self, numero2):
        self.numero2= numero2

    def suma(self):
        return self.numero1 + self.numero2
    
    def resta(self):
        return self.numero1 - self.numero2
    
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        if self.numero2== 0:
            print("No es posible una división entre cero")
        else:
            return self.numero1 / self.numero2

calculadora1 =calculadora()

numero1= float(input("Ingrese un numero: "))
numero2= float(input("Ingrese el segundo numero: "))

calculadora1.obtenernumero1(numero1)
calculadora1.obtenernumero2(numero2)

operacion = 0

while operacion != 5:
    print("______MENU DE OPERACIONES_____")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir del menu")

    operacion=int(input("Escoja una de las opciones: "))

    if operacion ==1:
        print(" La suma de ambos numero es: ", calculadora1.suma())
    elif operacion==2:
        print(" La resta de ambos numeros es: ", calculadora1.resta())
    elif operacion==3:
        print("La multiplicación de ambos número es: ", calculadora1.multiplicacion())
    elif operacion==4:
        print("La división de ambos números resulta en: ", calculadora1.division())
    elif operacion==5:
        print("Ha decidio salir del menú.")
    else:
        print("Opción incorrecta, selecciones nuevamente")