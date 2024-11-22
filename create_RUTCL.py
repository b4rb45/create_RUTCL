import random

def calcular_digito_verificador(rut):
    """
    Calcula el dígito verificador para un RUT chileno.
    """
    suma = 0
    multiplicador = 2

    for digito in reversed(str(rut)):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = 11 - (suma % 11)
    if resto == 11:
        return '0'
    elif resto == 10:
        return 'K'
    else:
        return str(resto)

def generar_ruts(cantidad, rut_min, rut_max):
    """
    Genera una lista de RUTs chilenos válidos.
    """
    ruts_generados = []
    for _ in range(cantidad):
        rut = random.randint(rut_min, rut_max)
        dv = calcular_digito_verificador(rut)
        ruts_generados.append(f"{rut}-{dv}")
    return ruts_generados

def main():
    print("Generador de RUTs Chilenos")
    try:
        cantidad = int(input("Ingrese la cantidad de RUTs a generar: "))
        rut_min = int(input("Ingrese el RUT mínimo (sin dígito verificador): "))
        rut_max = int(input("Ingrese el RUT máximo (sin dígito verificador): "))

        if rut_min >= rut_max:
            print("El RUT mínimo debe ser menor al RUT máximo.")
            return

        ruts = generar_ruts(cantidad, rut_min, rut_max)
        print("\nRUTs generados:")
        for rut in ruts:
            print(rut)

    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")

if __name__ == "__main__":
    main()
