import calculadora_indices as calc

print("Vamos a calcular tu IMC")
print("_______________________\n")
peso = float(input("Ingresá tu peso en kg: "))
altura = float(input("Ahora ingresa tu alura en metros: "))

imc = calc.calcular_IMC(peso, altura)

print(f"Tu IMC es de: {imc}")

print("Segun tus datos vos tenes...")
if imc < 16:
    print("Delgadez severa")
elif 16 <= imc < 17:
    print("Delgadez moderada")
elif 17 <= imc < 18.5:
    print("Delgadez aceptable")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidad tipo I")
elif 35 <= imc < 40:
    print("Obesidad tipo II")
elif 40 <= imc < 50:
    print("Obesidad tipo III o Mórbida")
elif 50 <= imc :
    print("Obesidad tipo IV o Extrema")
