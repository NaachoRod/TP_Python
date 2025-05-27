import calculadora_indices as calc

print("Vamos a calcular tu porcentaje de grasa corporal")
print("________________________________________________\n")

try:
    peso = float(input("Ingresá tu peso en kg: "))
    altura = float(input("Ingresa tu altura en metros: "))
    edad = int(input("Ingresa tu edad en años: "))

    genero = int(input("Ahora necesitamos tu género\n Para masculino ingresá 1\n Para femenino ingresá 2: "))
    while genero not in (1, 2):
        genero = int(input("Número incorrecto\n Para masculino ingresá 1\n Para femenino ingresá 2: "))

    genero_valor = 10.8 if genero == 1 else 0

    imc = calc.calcular_IMC(peso, altura)
    PGC = calc.calcular_porcentaje_grasa(imc, edad, genero_valor)

    print(f"\nTu PGC es de: {PGC:.2f}%")

    if genero == 1:
        print(f"\n{'Rango de edad':<15}{'%GC Hombres':<20}")
        print("-" * 40)
        print(f"{'20 - 29':<15}{'11% - 20%':<20}")
        print(f"{'30 - 39':<15}{'12% - 21%':<20}")
        print(f"{'40 - 49':<15}{'14% - 23%':<20}")
        print(f"{'50 - 59':<15}{'15% - 24%':<20}")
    else:
        print(f"\n{'Rango de edad':<15}{'%GC Mujeres':<20}")
        print("-" * 55)
        print(f"{'20 - 29':<15}{'16% - 28%':<20}")
        print(f"{'30 - 39':<15}{'17% - 29%':<20}")
        print(f"{'40 - 49':<15}{'18% - 30%':<20}")
        print(f"{'50 - 59':<15}{'19% - 31%':<20}")

except Exception as e:
    print(f"\nError inesperado: {e}")
