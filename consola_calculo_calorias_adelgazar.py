import calculadora_indices as calc


print("Vamos a calcular tu cuantas calorias necesitas para adelgazar")
print("________________________________________________\n")

peso = float(input("Ingresá tu peso en kg: "))
altura = int(input("Ingresa tu alura en centimetros (cm): "))
edad = int(input("Ingresa tu edad en años: "))
genero = int(input("Ahora necesitamos tu genero\n Para genero masculino ingresa 1\n Para genero femenino ingresa 2: "))
while genero != 1 and genero != 2:
    genero = int(input("Número incorrecto\n Para genero masculino ingresa 1\n Para genero femenino ingresa 2: "))

if genero == 1:
    genero_valor = 5 
else:
    genero_valor = -161

tmb = calc.caclular_calorias_en_reposo(peso, altura, edad, genero_valor)

cpa = calc.consumo_calorias_recomendado_para_adelgazar(tmb)

print(f"Para adelgazar es recomendado que consumas entre: {cpa[0]:.2f} y {cpa[1]:.2f} calorías al día.")