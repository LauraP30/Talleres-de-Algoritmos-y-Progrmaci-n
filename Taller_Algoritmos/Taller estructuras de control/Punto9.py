"""
Entradas
Sueldo-->int-->s
Horas-->int-->h
Salidas
Neto-->int-->sn
"""
s=int(input("Ingrese el salario: "))
h=int(input("Ingrese las horas trabajadas: "))
#caja negra
a=(1*s)/h
b=s*0.2
sn=s-b
#Salidas
print("El precio por hora es $","{:.0f}".format(a))
print("El salario neto es: $","{:.0f}".format(sn))
