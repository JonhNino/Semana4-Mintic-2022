#Programa para las operaciones entre conjuntos
# JOnh niño
# Hoyu

#Dados el conjunto A de N elementos enteros y el conjunto B de M elementos enteros
#Se pide:
#Generar conjunto C con la union de A y B
# Generra conjunto D con la interseccion de A y B
#Generar conjunt E con la diferencia entre A y B
#Generar Conjunto F con la diferncia entre B y A

A=set([])
B=set([])
 
 #Llenar los conjutnos
N=int(input("Cantdidad Elementos conjunto A"))
for i in range (N):
    numero=int(input("Numero: "))
    A.add(numero)
M=int(input("Cantidad de Elementos conjunto B: "))
for j in range(M):
    numero=int(input("Numero: "))
    B.add(numero)

#Procesar los conjuntos
C=A | B
D=A & B
E=A - B
F=B - A

print("A ",A)
print("B ",B)
print("C ",C)
print("D ",D)
print("E ",E)
print("F ",F)




