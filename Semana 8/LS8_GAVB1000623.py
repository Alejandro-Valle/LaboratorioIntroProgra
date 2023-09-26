#Introducción a la programación
#Alejandro Valle 1000623
#26/09/2023

print("Seleccione una de las siguientes opciones: 1. Factorial, 2. Secuencia de Fibonacci, 3. Salir")
operacion=input()

while operacion !="3":
    if operacion == "1":
        print("ingrese un valor")
        x=int(input(), base=0)
        factorial=1
        print("El factorial de dicho número es: ")
        for p in range (1,x+1):
            factorial= factorial * p
            print(factorial)


    if operacion =="2":
        print("ingrese un valor")
        y=int(input(), base=0)
        print("Fibonacci: ")
        a=0
        b=1
        for z in range (y):
            c=b+a
            a=b
            b=c
            print(a)

    if operacion == "3":
        print("Ha salido del menú")
    

        