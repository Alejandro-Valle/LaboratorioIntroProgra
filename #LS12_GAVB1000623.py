#LS12_GAVB1000623

class persona:
    nombres=""
    apellidos=""
    apellidocasada= ""
    fecha_de_nacimiento=""

    def ingresar_nombre(self, nombres):
        self.nombres = nombres

    def devolver_nombres(self):
        return self.nombres
    
    def ingresar_apellidos(self, apellidos):
        self.apellidos= apellidos

    def apellido_casada(self, apellidocasada):
        self.apellidocasada = apellidocasada
    
    def devolver_apellidos(self):
        if self.apellidocasada != "":
            return self.apellidos + self.apellidocasada
        else:
            return self.apellidos 

    def fecha_nacimiento(self, fecha_de_nacimiento):
        self.fecha_de_nacimiento = fecha_de_nacimiento
    
    def devolverfecha (self):
        return self.fecha_de_nacimiento
    
    def devolvernombrecompleto (self):
        return self.nombres +" "+ self.apellidos + self.apellidocasada
    
    
persona1 = persona()

persona1.ingresar_nombre("María Valeria")
print(persona1.devolver_nombres())

persona1.ingresar_apellidos("Valle Bances ")
print(persona1.devolver_apellidos())

persona1.fecha_nacimiento("16/07/2023")
print(persona1.devolverfecha())

persona1.apellido_casada(" de Garrido")
print(persona1.devolver_apellidos())

persona1.devolvernombrecompleto()
print(persona1.devolvernombrecompleto())


        