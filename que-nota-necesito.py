print("Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.")
C1 = float(input("Ingrese nota certamen 1: \n"))
C2 = float(input("Ingrese nota certamen 2: \n"))
Nl = float(input("Ingrese nota laboratorio: \n"))

C3 =  float(3*((60 - Nl*0.3)//0.7) - (C1 + C2))

print(f"Necesita nota {C3} en el certamen 3")
