print(f"Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso: \n")


numero = input("Ingresa un número entero de tres dígitos: ")


if len(numero) == 3 and numero.isdigit():
    
    numero_invertido = numero[2] + numero[1] + numero[0]
    print(f"El número invertido es: {numero_invertido}")
else:
    print("Por favor, ingresa un número entero de tres dígitos.")