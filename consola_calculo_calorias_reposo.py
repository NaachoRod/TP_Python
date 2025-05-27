import calculadora_indices as calc

print("Vamos a calcular tu Tasa Metabólica Basal")
print("________________________________________________\n")

try:
    peso = float(input("Ingresá tu peso en kg: "))
    altura = int(input("Ingresá tu altura en centímetros (cm): "))
    edad = int(input("Ingresá tu edad en años: "))

    genero = int(input("Ahora necesitamos tu género\n Para género masculino ingresá 1\n Para género femenino ingresá 2: "))
    while genero != 1 and genero != 2:
        genero = int(input("Número incorrecto\n Para género masculino ingresá 1\n Para género femenino ingresá 2: "))

    genero_valor = 5 if genero == 1 else -161

    tmb = calc.caclular_calorias_en_reposo(peso, altura, edad, genero_valor)

    print(f"\nTu TMB es de: {tmb:.2f} calorías")

except Exception as e:
    print(f"\nError inesperado: {e}")
