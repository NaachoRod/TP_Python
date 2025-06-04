import calculadora_indices as calc

print("Vamos a calcular tu TMB según Actividad Física")
print("________________________________________________\n")

try:
    peso = float(input("Ingresá tu peso en kg: "))
    altura = int(input("Ingresa tu altura en centímetros (cm): "))
    edad = int(input("Ingresa tu edad en años: "))
    
    genero = int(input("Ahora necesitamos tu género\n Para género masculino ingresa 1\n Para género femenino ingresa 2: "))
    while genero != 1 and genero != 2:
        genero = int(input("Número incorrecto\n Para género masculino ingresa 1\n Para género femenino ingresa 2: "))

    if genero == 1:
        genero_valor = 5 
    else:
        genero_valor = -161

    tmb = calc.caclular_calorias_en_reposo(peso, altura, edad, genero_valor)

    print(f"\nAhora necesitamos saber cuánta actividad física realizás por semana\n")
    print("_" * 20)
    print("\nOpciones:")
    print("_" * 20)
    print("1: poco o nada")
    print("2: ejercicio ligero (1 a 3 días a la semana)")
    print("3: ejercicio moderado (3 a 5 días a la semana)")
    print("4: deportista (6 a 7 días a la semana)")
    print("5: atleta (entrenamientos mañana y tarde)")

    opcion = int(input("Ingresá una opción (1 a 5): "))
    while opcion < 1 or opcion > 5:
        opcion = int(input("Opción inválida. Ingresá un número del 1 al 5: "))

    if opcion == 1:
        nivel_actividad = 1.2
    elif opcion == 2:
        nivel_actividad = 1.375
    elif opcion == 3:
        nivel_actividad = 1.55
    elif opcion == 4:
        nivel_actividad = 1.725
    else:
        nivel_actividad = 1.9

    tmbaf = calc.calcular_calorias_en_actividad(tmb, nivel_actividad)
    print(f"\nTu TMB según Actividad Física es de: {tmbaf:.2f} calorías")

except Exception as e:
    print(f"\nError inesperado: {e}")
