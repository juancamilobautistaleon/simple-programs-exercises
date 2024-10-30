import math 
TO = float(input("Ti \n"))
TW = 100
TY = 70
M = 47
P = 1.038
C = 3.7
K = 5.4 * math.pow(10, -3)


Dividendo   = math.pow(M, (2/3)) * (C * (math.pow(P, (1/3))))
Divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))

resultado = Dividendo/Divisor

resultado2 = math.log(0.76 * ((TO - TW ) / (TY - TW)))

segundos = resultado * resultado2/60

print(f"El tiempo para prepararlo es {segundos} minutos")