


def calcular_IMC(peso, altura):
    if peso <= 0 or altura <= 0:
        raise Exception("El Peso o Altura no pueden ser 0 o menor")
    else:
        imc = peso / altura**2
    return imc
    

def calcular_porcentaje_grasa(imc, edad, genero):
    if edad <= 0:
        raise Exception("La Edad no pueden ser 0 o menor")
    PGC = 1.2 * imc + 0.23 * edad -5.4 - genero
    return PGC

def caclular_calorias_en_reposo(peso, altura, edad, genero):
    if peso <= 0 or altura <= 0 or edad <= 0:
        raise Exception("El Peso, Altura o Edad no pueden ser 0 o menor")
    tmb = 10 * peso + 6.25 * altura - 5 * edad + genero
    return tmb

def calcular_calorias_en_actividad(tmb, actividad):
    tmbaf = tmb * actividad
    return tmbaf

def consumo_calorias_recomendado_para_adelgazar(tmb):
    minimo = tmb * 0.80
    maximo = tmb * 0.85
    return minimo, maximo
