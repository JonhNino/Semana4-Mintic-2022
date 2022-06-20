# Programa para manejo de listas dentro de listas (Matrices)
# JOnh Niño
# Hoy
matriz=[]
cantidad_pares=0
cantidad_impares=0
#Llenar lista dentro de lista

for i in range(2):
    matriz.append([])
    for j in range (2):
        numero=int(input("Numero Entero: "))
        matriz[i].append(numero)
print(matriz)

#Procesar

for x in range(2):
    for y in range(2):
        if matriz[x][y]%2==0:
            cantidad_pares+=1
        else:
            cantidad_impares+=1
print("Impares",cantidad_impares)
print("Pares",cantidad_pares)