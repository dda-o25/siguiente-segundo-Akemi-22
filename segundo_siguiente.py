"""
Akemi Clarissa Olvera Arao
19/09/25
Calcular lo hora un segundo después
"""

# Declaraciones


# Entradas
hora = int(input("Ingrese una hora: "))
minuto = int(input("Ingrese un minuto: "))
segundo = int(input("Ingrese un segundo: "))
print("Hora inicial: \nHora: ", hora, "\nMinuto: ", minuto, "\nSegundo: ", segundo)

# Proceso
segundo += 1
if segundo >= 60:
    segundo = 0
    minuto += 1
    if minuto >= 60:
        minuto = 0
        hora +=1
        if hora >=24:
            hora = 0


# Salidas
print("Hora final: \nHora: ", hora, "\nMinuto: ", minuto, "\nSegundo: ", segundo)