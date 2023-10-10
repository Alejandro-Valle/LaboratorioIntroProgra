#LS10_GAVB1000623

def letrahexadecimal(num1):
    num1 = str(num1)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if num1 in equivalencias:
        return equivalencias[num1]
    else:
        return num1


def numerohexadecimal(numero):
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        verdadero_caracter = letrahexadecimal(residuo)
        hexadecimal = verdadero_caracter + hexadecimal
        numero = int(numero / 16)
    return hexadecimal


numero = int(
    input("Ingrese un número: "))
hexadecimal = numerohexadecimal(numero)
print("EL número en hexadecimal es: "+ hexadecimal)