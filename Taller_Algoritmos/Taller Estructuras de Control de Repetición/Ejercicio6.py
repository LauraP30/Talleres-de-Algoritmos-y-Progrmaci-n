"""
Entradas
Numerador-->int-->a
Denominador-->int-->b
Salidas
Resta-->int-->a
"""
c=0
r=0
a=int(input("Ingrese el numerador: "))
b=int(input("Ingrese el denominador: "))
while(a>=b):
  a=a-b
  r=a
  print(a)