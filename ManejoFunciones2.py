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

    return tarifa_Basica,valor_impulsos,valor_abonado

def valida_entero(etiqueta):
    while True:
        try:
            dato=int(input(etiqueta))
            break
        except ValueError:
            print(etiqueta," Debe ser un dato entero")
    return dato

def valida_estrato(etiqueta):
    while True:
        try:
            estrato=int(input(etiqueta))
            if estrato<1 or estrato>5:
                print(etiqueta,"debe estar entre 1 y 5")
                continue
            break
        except ValueError:
            print(etiqueta," Debe ser un dato entero")
    return estrato


#Programa Principal
N=valida_entero("Cantidad de abonados")
total_abonados=0
for i in range(N):
    nombre=input("Nombre abonado")
    estrato=valida_estrato("Estrato")
    impulsos=valida_entero("Cantidad de impulsos")
    #Llamado de la Funcion
    tarifa_Basica,valor_impulsos,valor_abonado=Facturacion_Abonado(estrato, impulsos)
    total_abonados+=valor_abonado
    print(nombre)
    print("{:,.2f}".format(tarifa_Basica))
    print("{:,.2f}".format(valor_impulsos))
    print("{:,.2f}".format(valor_abonado))
print("{:,.2f}".format(total_abonados))