"""
Conversión de Números:
Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.
"""
def decimal_a_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario  # Devuelvo el resultado

opcion = input("Seleccione una opcion para convertir:\n1. Decimal a Binario\n2. Binario a Decimal\nO ingrese cualquier otro caracter para terminar el programa\nOpcion: ")

if opcion == '1':
    a = True
    while a:
        numero = input("Ingrese un numero decimal positivo: ")
        if not numero.isdigit() or int(numero) < 0:
            print("Error: Debe ingresar un numero entero positivo.")
        else:
            a = False  # Entrada válida
    numero = int(numero)
    if numero == 0:
        print("El numero binario es: 0")
    else:
        resultado = decimal_a_binario(numero)
        print("El numero binario es:", resultado, "\n programa terminado.")

elif opcion == '2':
    a = True
    while a:
        numero = input("Ingrese un numero binario: ")
        es_binario = True
        for bit in numero:
            if bit != '0' and bit != '1':
                es_binario = False
        if not es_binario:
            print("Error: Debe ingresar un numero binario valido (solo 0s y 1s).")
        else:
            a = False  # si la entrada es valida entonces salgo del bucle
    if numero == "0":
        print("El numero a decimal es: 0")
    else:
        resultado = 0 #voy guardando el numero aca
        potencia = 0 #indica la posicion del bit
        numero = int(numero)
        while numero > 0:
            resultado += (numero % 10) * (2 ** potencia) #calcula la potencia de 2 que corresponde a la posicion del bit
            numero //= 10 # divido el numero por 10 para ir eliminando los bits
            potencia += 1
        print("El numero a decimal es:", resultado, "\n programa terminado.")

else:
    print("Programa terminado. Gracias por usar el conversor de numeros.")

