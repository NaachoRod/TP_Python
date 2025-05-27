import calculadora_indices as calc

print("Vamos a calcular cuántas calorías necesitás para adelgazar")
print("________________________________________________\n")

try:
    peso = float(input("Ingresá tu peso en kg: "))
    altura = int(input("Ingresá tu altura en centímetros (cm): "))
    edad = int(input("Ingresá tu edad en años: "))
    
    genero = int(input("Ahora necesitamos tu género\n Para género masculino ingresá 1\n Para género femenino ingresá 2: "))
    while genero != 1 and genero != 2:
        genero = int(input("Número incorrecto\n Para género masculino ingresá 1\n Para género femenino ingresá 2: "))

    if genero == 1:
        genero_valor = 5 
    else:
        genero_valor = -161

    tmb = calc.caclular_calorias_en_reposo(peso, altura, edad, genero_valor)
    cpa = calc.consumo_calorias_recomendado_para_adelgazar(tmb)

    print(f"\nPara adelgazar se recomienda consumir entre: {cpa[0]:.2f} y {cpa[1]:.2f} calorías al día.")

except Exception as e:
    print(f"\nError inesperado: {e}")
