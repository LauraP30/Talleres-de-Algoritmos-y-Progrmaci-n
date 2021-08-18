"""
Entradas
Compra-->int-->a
Salidas
Total-->int-->c
"""
a=int(input("Digite el valor de la compra: "))
#caja negra
b=a*0.15
c=a-b
#Salidas
print(("El total es: $"),"{:.0f}".format(c))
