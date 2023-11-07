#LS14_GAVB1000623

class automovil:
    def __init__(self):
        self.modelo=0
        self.precio=0.0
        self.marca=""
        self.disponible=True
        self.tipocambiodolar=0.0
        self.descuentoaplicado=0.0
    
    def definirmodelo(self, unmodelo):
        self.modelo=unmodelo
    
    def definirprecio(self, unprecio):
        self.precio=unprecio
    
    def definirmarca(self, unamarca):
        self.marca=unamarca
    
    def definirtipocambio(self, untipocambio):
        self.tipocambiodolar=untipocambio
    
    def preciodolares(self):
        return self.precio*self.tipocambiodolar

    def cambiardisponibilidad(self):
        if self.disponible == True:
            self.disponible = False
        elif self.disponible==False:
            self.disponible = True
    

    def mostrarinformacion(self):
        return print("Marca: " + str(self.marca) + ". Modelo: "+str(self.modelo)+". Precio de  venta: Q"+str(self.precio)+". Precio en dolares $"+str(self.preciodolares())+". "+str(self.mostrardisponibilidad()))

    def aplicardescuento(self, midescuento):
        self.descuentoaplicado=midescuento

    def definirpreciodescuento(self, midescuento):
        self.precio=(self.precio)-(self.precio*midescuento) 
    
    def mostrardisponibilidad(self):
        if self.disponible==True:
            return "Disponible"
        elif self.disponible==False:
            return "No se encuentra disponible actualmente. "
    
carro1= automovil()
carro1.definirmodelo(2004)
carro1.definirprecio(50000.95)
carro1.definirmarca("Toyota")
carro1.definirtipocambio(7.8)
carro1.definirpreciodescuento(0.9)
carro1.mostrarinformacion()