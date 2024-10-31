
hora_actual = input("Ingresa la hora actual (HH:MM:SS): ")


horas_a_sumar = int(input("Ingresa el número de horas a sumar: "))

hora = int(hora_actual[0:2])  
minuto = int(hora_actual[3:5])  
segundo = int(hora_actual[6:8])  


if 0 <= hora < 24 and 0 <= minuto < 60 and 0 <= segundo < 60:
    
    nueva_hora = (hora + horas_a_sumar) % 24
    
    nueva_minuto = minuto
    nueva_segundo = segundo

    
    print(f"La nueva hora será: {nueva_hora:02d}:{nueva_minuto:02d}:{nueva_segundo:02d}")
else:
    print("Por favor, ingresa una hora válida en formato HH:MM:SS.")