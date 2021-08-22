"""
Entradas
a-->int-->A
b-->int-->B
c-->int-->C
d-->int-->D
Salidas
Resultado-->int-->r
"""
A=int(input("Ingrese el valor de A: "))
B=int(input("Ingrese el valor de B: "))
C=int(input("Ingrese el valor de C: "))
D=int(input("Ingrese el valor de D: "))
if(D==0):
  r=(A-C)**2
elif(D>0):
  r=(A-B)**3/D
print("El resultado es: ","{:.0f}".format(r))