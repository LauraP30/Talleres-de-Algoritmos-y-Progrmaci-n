"""
Entradas
Prestamo-->int-->a
Salidas
Porcentaje-->int-->b
"""
a=int(input("Ingrese el valor del prestamo: "))
#caja negra
t=4
r=1
I=(a*t*r)/100
b=(I*100)/a
#Salidas
print("Cobraron anualmente un ","{:.0f}%".format(b))
