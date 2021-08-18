"""
Entradas
Contado-->int-->P
Cuotas-->int-->T
Salidas
Porcentaje-->int-->C
"""
P=int(input("Ingrese el valor al contado: "))
T=int(input("Ingrese el valor por 12 cuotas: "))
#caja negra
a=T-P
b=(a*100)/T
C=b/12
#Salidas
print("EL recargo por cuota es: ","{:.0f}%".format(C))
