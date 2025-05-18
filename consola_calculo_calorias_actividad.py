import calculadora_indices as calc

print("Vamos a calcular tu TMB según Actividad Física")
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

print(f"\nAhora necesitamos saber cuanta actividad física realizas por semana\n")
print("_" * 20)
print("\nOpciones:")
print("_" * 20)
print("\n1: poco o nada\n")
print("2: ejercicio ligero(1 a 3 días a la semana)\n")
print("3: ejercicio moderado (3 a 5 días a la semana)\n")
print("4: deportista (6 a 7 días a la semana)\n")
print("5: atleta (entrenamientos mañana y tarde)\n")

opcion = int(input("Ingresá una opción (1 a 5): "))

while opcion < 1 or opcion > 5:
    opcion = int(input("Opción inválida. Ingresá un número del 1 al 5: "))

# Asignar el valor correspondiente
if opcion == 1:
    nivel_actividad = 1.2
elif opcion == 2:
    nivel_actividad = 1.375
elif opcion == 3:
    nivel_actividad = 1.55
elif opcion == 4:
    nivel_actividad = 1.72
else:
    nivel_actividad = 1.9

tmbaf = calc.calcular_calorias_en_actividad(tmb, nivel_actividad)

print(f"\nTu TMB según Actvidad Física es de: {tmbaf} calorias")