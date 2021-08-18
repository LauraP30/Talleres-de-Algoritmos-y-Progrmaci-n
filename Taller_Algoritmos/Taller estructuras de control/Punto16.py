"""
Entradas
Galon-->int-->a
Salidas
Cobro-->int-->c
"""
a=int(input("Ingrese los galones: "))
#caja negra
g=3.785
l=50000
b=a*g
c=b*l
#Salidas
print("El cobro es: $","{:.0f}".format(c))
