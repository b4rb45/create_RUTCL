import random

def generar_rut(rut_minimo, rut_maximo):
    # Generar números aleatorios para el RUT
    rut = random.randint(rut_minimo, rut_maximo)
    
    # Calcular el dígito verificador
    multiplicadores = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    for i in range(8):
        suma += int(str(rut)[::-1][i]) * multiplicadores[i]
    digito_verificador = 11 - (suma % 11)
    if digito_verificador == 10:
        digito_verificador = 'K'
    elif digito_verificador == 11:
        digito_verificador = 0
    
    # Formatear el RUT
    rut_formateado = f"{rut}-{digito_verificador}"
    
    return rut_formateado

# Solicitar la cantidad de RUT y el rango
cantidad_rut = int(input("Ingrese la cantidad de RUT a generar: "))
rut_minimo = int(input("Ingrese el valor mínimo para el RUT: "))
rut_maximo = int(input("Ingrese el valor máximo para el RUT: "))

# Generar los RUT válidos
for _ in range(cantidad_rut):
    rut_valido = generar_rut(rut_minimo, rut_maximo)
    print(rut_valido)
