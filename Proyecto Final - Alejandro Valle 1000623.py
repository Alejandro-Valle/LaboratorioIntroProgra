'''Alejandro Valle 1000623
P2_GAVB1000623'''
letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}

class Tablero():
    def __init__(self):
        self.filas = 10
        self.columnas = 10
        self.tablero = []
        self.crear_tablero()

    def crear_tablero(self):
        for i in range(self.filas):
            self.tablero.append([])
            for j in range(self.columnas):
                self.tablero[i].append("O")

    def get_casilla(self, filequequiero, columnaquequiero):
        return self.tablero[filequequiero][columnaquequiero]

    def set_casilla(self, fila, columna, valor):
        self.tablero[fila][columna] = valor
    
    def imprimir_tablero(self):
        print("  1 2 3 4 5 6 7 8 9 10")
        for i in range(self.filas):
            columna ='ABCDEFGHIJ'[i]
            print(columna, end=" ")
            for j in range(self.columnas):
                print(self.tablero[i][j], end=" ")
            print()

    def verificar_grande(self, x,y, orientacion_new): 
        if x <= 10 or y <= 10:
            if orientacion_new == "H":
                if x + 5 <= 10:
                    return True
                else:
                    return False
            elif orientacion_new == "V":
                if y + 5 <= 10:
                    return True
                else:
                    return False
        else:
            return False 
    
    def verificar_pequeno(self, x,y, orientacion_new): 
        if x <= 10 or y <= 10:
            if orientacion_new == "H":
                if x + 3 <= 10:
                    return True
                else:
                    return False
            elif orientacion_new == "V":
                if y + 3 <= 10:
                    return True
                else:
                    return False 
            else:
                return False
                
    def set_barco_grande(self, x, y, orientacion):         
        if self.verificar_grande(x,y,orientacion):
            # Poner los barcos
            if orientacion == "H":
                for i in range(5):
                    self.set_casilla(y, x+i, "?")
            elif orientacion == "V":
                for i in range(5):
                    self.set_casilla(y+i, x, "?")
            self.imprimir_tablero()
        else: 
            print("Se paso")

    def set_barco_pequeno(self, x, y, orientacion): 
        print("Agregando Barco pequeño") 
        if self.verificar_grande(x,y,orientacion):
            # Poner los barcos
            if orientacion == "H":
                for i in range(3):
                    self.set_casilla(y, x+i, "?")
            elif orientacion == "V":
                for i in range(3):
                    self.set_casilla(y+i, x, "?")
            self.imprimir_tablero()
        else: 
            print("Se paso")

class Jugador(): 
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0 # Porque se empieza con 0
        self.new_tablero = Tablero()

    def get_nombre(self):
        return self.nombre

 
def start_game(jugador1, jugador2): 
    print("**** INICIAR JUEGO ********")
    juego_terminado = False 
    while(juego_terminado == False):
        # Turno JUGADOR 1 
        print("Turno de  " + str(jugador1.nombre))
        tiro = input("Ingrese coordenadas >")
        tiro_y = letter_to_number[tiro[0].capitalize()]
        tiro_x = int(tiro[1])
        tiro_x-=1
        tiro_y-=1
       
        # Verificar si le dio a un barco
        if jugador2.new_tablero.get_casilla(tiro_y, tiro_x) == "?":
            print("Le diste a un barco")
            jugador1.puntaje += 1
            jugador2.new_tablero.set_casilla(tiro_y, tiro_x, "X")
            jugador2.new_tablero.imprimir_tablero()
        else:
            print("Has Fallado el disparo. ")
        
        # Verificacion de juego terminado
        if jugador1.puntaje == 19:
            print(str(jugador1.nombre) + " gano")
            juego_terminado = True
            break
        elif jugador2.puntaje == 19:
            print(str(jugador2.nombre)+  "gano")
            juego_terminado = True
            break
        else:
            print("Sigue jugando") 

        # Turno JUGADOR 2 
        print("Turno de " + str(jugador2.nombre))
        tiro = input("Ingrese coordenadas >")
        tiro_y = letter_to_number[tiro[0].capitalize()]
        tiro_x = int(tiro[1])
        tiro_x-=1
        tiro_y-=1
        # Verificar si le dio a un barco
        if jugador1.new_tablero.get_casilla(tiro_y, tiro_x) == "?":
            print("Le diste a un barco")
            jugador2.puntaje += 1
            jugador1.new_tablero.set_casilla(tiro_y, tiro_x, "X")
            jugador1.new_tablero.imprimir_tablero()
        else:
            print("Has fallado el disparo")

        # Verificacion de juego terminado
        if jugador1.puntaje == 19:
            print(str(jugador1.nombre)+" ganó")
            juego_terminado = True
            break
        elif jugador2.puntaje == 19:
            print(str(jugador2.nombre)+" ganó")
            juego_terminado = True
            break
        else:
            print("Sigue jugando")

def create_game():
    print("**** COLOCAR JUGADORES ********")
    # Instanciar jugadores 
    nombre = input("Jugador 1 - Ingrese nombre > ")
    jugador1 = Jugador(nombre)
    nombre = input("Jugador 2 - Ingrese nombre > ")
    jugador2 = Jugador(nombre)
    # Crear tableros de Jugadores 
    jugador1.new_tablero.crear_tablero() 
    jugador2.new_tablero.crear_tablero()
    print("Tableros creados")
    print("jugador1->")
    jugador1.new_tablero.imprimir_tablero()
    print("jugador2->")
    jugador2.new_tablero.imprimir_tablero()

    # Colocar Barcos 
    print("**** COLOCAR BARCOS ********")
    print("Turno de  "+ str(jugador1.nombre))
    print("Colocar Barcos Grandes")
    
    # Como hay que repetirlo 5 veces 
    contador_grandes = 0 
    while(contador_grandes <2):
        coordenada = input("Ingrese coordenadas >")
        new_coordenada = coordenada.strip() #-> Error
        y = letter_to_number[coordenada[0].capitalize()]
        x = int(coordenada[1])
        x-=1
        y-=1
        orientacion_solicitada= input("Ingrese la orientacion (V/H): ")
        print(orientacion_solicitada.capitalize())
        # Pedir orientacion del barco
        jugador1.new_tablero.set_barco_grande(x,y,orientacion_solicitada.capitalize())
        contador_grandes= contador_grandes + 1
    print("Colocar Barcos Pequeños")
    
    contador_pequeños = 0 
    # Como hay que repetirlo 3 veces 
    while(contador_pequeños < 3):
        coordenada = input("Ingrese coordenadas >")
        new_coordenada = coordenada.split() #-> Error
        y = letter_to_number[coordenada[0].capitalize()]
        x = int(coordenada[1])
        x-=1
        y-=1
        orientacion_solicitada= input("Ingrese la orientacion (V/H): ")
        # Pedir orientacion del barco
        jugador1.new_tablero.set_barco_pequeno(x,y,orientacion_solicitada.capitalize())
        contador_pequeños+= 1
    
    print("Turno de  "+str(jugador2.nombre))
    print("Colocar Barcos Grande")
    contador = 0 
    # Como hay que repetirlo 5 veces 
    while(contador < 2):
        coordenada = input("Ingrese coordenadas >")
        new_coordenada = coordenada.split() #-> Error
        y = letter_to_number[coordenada[0].capitalize()]
        x = int(coordenada[1])
        x-=1
        y-=1
        orientacion_solicitada= input("Ingrese la orientacion (V/H): ")
        # Pedir orientacion del barco
        jugador2.new_tablero.set_barco_grande(x,y,orientacion_solicitada.capitalize())
        contador += 1
    print("Colocar Barcos Pequeños")
    
    contador = 0
    # Como hay que repetirlo 3 veces 
    while(contador < 3):
        coordenada = input("Ingrese coordenadas >")
        new_coordenada = coordenada.split() #-> Error
        y = letter_to_number[coordenada[0].capitalize()]
        x = int(coordenada[1])
        x-=1
        y-=1
        orientacion_solicitada= input("Ingrese la orientacion (V/H): ")
        # Pedir orientacion del barco
        jugador2.new_tablero.set_barco_pequeno(x,y,orientacion_solicitada.capitalize())
        contador += 1
    
    # YA estan puestos los barcos ----- 
    start_game(jugador1, jugador2)
    
def menu():
    print("------- BATALLA NAVAL -------")
    print("*** Alejandro Valle ******")
    print("1. Iniciar Juego")
    print("2. Salir del Juego")
    opcion = input("Escoja una de las opciones:  ")

    if opcion == "1":
        create_game()
    elif opcion == "2":
        print("Ha decidido salir del Juego")
        exit 
    else:
        print("Opcion no valida")
        menu()

def main():
    menu()

if __name__ == "__main__":
    main()
