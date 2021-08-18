"""
Entradas
Metros-->float-->m
Salidas
Pulgadas-->float-->a
Pies-->float-->b
"""
m=float(input("Digite los metros: "))
#caja negra
a=m*39.27
b=a/12
#Salidas
print("Las pulgadas son: ","{:.3f}".format(a))
print("Los pies son: ","{:.3f}".format(b))
