import calculadora_indices as calc

print("Vamos a calcular tu porcentaje de grasa corporal")
print("________________________________________________\n")

peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ingresa tu alura en metros: "))
edad = int(input("Ingresa tu edad en años: "))
genero = int(input("Ahora necesitamos tu genero\n Para genero masculino ingresa 1\n Para genero femenino ingresa 2: "))
while genero != 1 and genero != 2:
    genero = int(input("Número incorrecto\n Para genero masculino ingresa 1\n Para genero femenino ingresa 2: "))

if genero == 1:
    genero_valor = 10.8  
else:
    genero_valor = 0

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
elif genero == 2:
    print(f"\n{'Rango de edad':<15}{'%GC Mujeres':<20}")
    print("-" * 55)
    print(f"{'20 - 29':<15}{'16% - 28%':<20}")
    print(f"{'30 - 39':<15}{'17% - 29%':<20}")
    print(f"{'40 - 49':<15}{'18% - 30%':<20}")
    print(f"{'50 - 59':<15}{'19% - 31%':<20}")


