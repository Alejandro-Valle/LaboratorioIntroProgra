#Operaciones aritmeticas, 
print("Ejercicio 1: Operaciones aritmeticas")

print("Escoga una opción: 1. Suma"," 2. Resta", " 3. Multiplicación"," 4. División"," 5. Modulo"," 6.Exponente"," 7.Cociente", " 8. finalizar programa")
operacion=input()
while operacion!="8":
    print("Escriba un valor para x: ")
    x=input()
    print("Escriba un valor para y: ")
    y=input()
    x2=int(x)
    y2=int(y)
    suma=x2+y2
    resta=x2-y2
    multi=x2*y2
    divi=x2/y2
    modulo=x2%y2
    exp=x2**y2
    cociente=x2//y2
    if(operacion=="1"):
     print(x+" + "+y+" = "+str(suma))
    if(operacion=="2"):
        print(x+" - "+y+" = " +str(resta))
    if(operacion=="3"):
        print(x+" * "+y+" = " +str(multi))
    if(operacion=="4"):
        print(x+" / "+y+" = " +str(divi))
    if(operacion=="5"):
        print(" El residuo entre x y y = " +str(modulo))
    if(operacion=="6"):
        print(x+" elevado a "+y+" = " +str(exp))
    if(operacion=="7"):
        print("El cociente de X y y = " +str(cociente))
       
    operacion=input()

