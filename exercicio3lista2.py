# Velocidades em km/h
velocidade_luz = 1079252847
velocidade_som = 1233

# Função para calcular o máximo divisor comum (MDC)
def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Cálculo do MDC
mdc_valor = mdc(velocidade_luz, velocidade_som)

# Cálculo do MMC
mmc = (velocidade_luz * velocidade_som) // mdc_valor

print("O MMC entre a velocidade da luz e do som é:", mmc)
