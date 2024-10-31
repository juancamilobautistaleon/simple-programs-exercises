import math

print("Programa que reciba como entrada el radio de un círculo y entrega como salida su perímetro y su área")
radio = float(input("\n Radio del circulo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio **2

print(f"El perimetro del circulo es de {perimetro}\nEl area del circulo es de {area}")