#Manejo De Funciones
#Jonh Niño
#Fecha Hoy

#Definicion Funciones
def Facturacion_Abonado (estrato, impulsos):
    if estrato ==1:
        tarifa_Basica=10000
    elif estrato ==2:
        tarifa_Basica=15000
    elif estrato ==3:
        tarifa_Basica=20000
    elif estrato ==4:
        tarifa_Basica=25000
    else :
        tarifa_Basica=30000

    valor_impulsos=impulsos*100
    valor_abonado=tarifa_Basica+valor_impulsos

    return valor_abonado

#Programa Principal

N=int(input("Cantidad Abonados"))
total_abonados=0
for i in range(N):
    nombre=input("Nombre abonado")
    estrato=int(input("Estrato"))
    impulsos=int(input("Impulsos"))
    #Llamado de la Funcion
    valor_abonado=Facturacion_Abonado(estrato, impulsos)
    total_abonados+=valor_abonado
    print(nombre)
    print("{:,.2f}".format(valor_abonado))
print("{:,.2f}".format(total_abonados))

