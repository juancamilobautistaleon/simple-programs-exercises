import math


a = float(input("Ingresa la longitud del cateto a: "))
b = float(input("Ingresa la longitud del cateto b: "))


c = math.sqrt(a**2 + b**2)

print(f"La longitud de la hipotenusa c es: {c:.2f}")