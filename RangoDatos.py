n = int(input("Ingrese la cantidad de datos: "))
datos = []

for i in range(n):
    dato = float(input(f"Ingrese el dato #{i + 1}: "))
    datos.append(dato)

minimo = min(datos)
maximo = max(datos)

rango = maximo - minimo

print(f"El rango de los datos ingresados es: {rango}")