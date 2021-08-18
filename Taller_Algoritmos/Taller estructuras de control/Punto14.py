"""
Entradas
Actual-->int-->lac
Anterior-->int-->lan
Kilovaltio-->float-->k
Salidas
Total-->int-->t
"""
lac=int(input("Ingrese la lectura actual: "))
lan=int(input("Ingrese la lectura anterior: "))
k=float(input("Ingrese el costo por kilovaltio: "))
#caja negra
a=lac-lan
t=a*k
#Salidas
print("EL total a pagar es: $","{:.0f}".format(t))
