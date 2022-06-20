#Manerjo de diccionarios
#Jonh Niño
#HOy

diccionario_categoria={1:25000,2:30000,3:40000,4:45000,5:60000}
N=int(input("Cantidad Docentes "))
total_honorarios=0
for i in range (N):
    cedula=int(input("Cedula Docente: "))
    nombre=input("Nombre Docente: ")
    categoria=int(input("Categoria: "))
    horas=int(input("Horas laborada en mes: "))
    honorarios=horas*diccionario_categoria.get(categoria)
    total_honorarios+=honorarios
    print("nombre Docente: ",nombre)
    print("Honorarios: ",honorarios)
print("Total Honorarios: ",total_honorarios)