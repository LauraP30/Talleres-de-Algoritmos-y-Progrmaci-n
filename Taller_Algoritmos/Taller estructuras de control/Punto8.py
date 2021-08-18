"""
Entradas
Lados-->int-->l
Salidas
Area-->int-->Ar
"""
l=input("Digite los lados: ").split(" ")
a,b,c=l
a=int(a)
b=int(b)
c=int(c)
#caja negra
import math
s=(a+b+c)/2
Ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
#Salidas
print("El area es: ","{:.2f}".format(Ar))
