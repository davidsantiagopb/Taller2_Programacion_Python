positivos = 0
negativos = 0

print("Ingresa varios valores enteros (ingresa 0 para terminar):")

while True:
    numero = int(input())
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        break

print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)

print("Gráfico de números positivos:", "*" * positivos)
print("Gráfico de números negativos:", "*" * negativos)