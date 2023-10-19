#LS11_GAVB1000623

caracteres= input("Ingrese distintos caracteres: ")

unos=0
ceros=0
otros=0

for caracter in caracteres:
    if caracter == "1":
        unos= unos + 1
    elif caracter == "0":
        ceros= ceros + 1
    else:
        otros= otros + 1

print("Cadena:   " + caracteres)
print(" Cantidad 0: " + str(ceros))
print(" Cantidad 1: " + str(unos))
print(" Otros caracteres: " + str(otros))