#Manerjo de diccionarios
#Jonh Niño
#HOy

diccionario_categoria={1:25000,2:30000,3:40000,4:45000,5:60000}
N=int(input("Cantidad Docentes "))
total_honorarios=0
for i in range (N):
    cedula=int(input("Cedula Docente: "))
    nombre=input("Nombre Docente: ")

    while True:
        try:
            categoria=int(input("Categoria: "))
            if diccionario_categoria.get(categoria,"Error")=="Error":
                print("Categoria no existe")
                continue
            break
        except ValueError:
            print("la Categofia debe ser un dato Entero")
    horas=int(input("Horas laborada en mes: "))
    honorarios=horas*diccionario_categoria.get(categoria)
    total_honorarios+=honorarios
    print("nombre Docente: ",nombre)
    print("Honorarios: ","{:,.2f}".format(honorarios))
print("Total Honorarios: ","{:,.2f}".format(total_honorarios))