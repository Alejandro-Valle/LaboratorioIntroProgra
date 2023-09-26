#Alejandro Valle 

print("Seleccione una de las siguientes opciones: 1. Factorial, 2. Secuencia de Fibonacci, 3. Salir")
operacion=input()

if operacion == "1":
    print("ingrese un valor")
    x=int(input(), base=0)
    print("El factorial de dicho número es: ")
    for p in range (x):
        resultado=(p-1)*(p-2)
        print(resultado)


if operacion =="2":
    print("ingrese un valor")
    y=int(input(), base=0)
    print("Fibonacci: ")
    for z in range (y):
        resultado=(z-1)+(z-2)
        print(resultado)

if operacion == "3":
    print("Ha salido del menú")
        