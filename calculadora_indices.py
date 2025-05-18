


def calcular_IMC(peso, altura):
    imc = peso / altura**2
    return imc
    

def calcular_porcentaje_grasa(imc, edad, genero):
    PGC = 1.2 * imc + 0.23 * edad -5.4 - genero
    return PGC

def caclular_calorias_en_reposo(peso, altura, edad, genero):
    tmb = 10 * peso + 6.25 * altura - 5 * edad + genero
    return tmb

def calcular_calorias_en_actividad(tmb, actividad):
    tmbaf = tmb * actividad
    return tmbaf

def consumo_calorias_recomendado_para_adelgazar(tmb):
    minimo = tmb * 0.80
    maximo = tmb * 0.85
    return minimo, maximo
