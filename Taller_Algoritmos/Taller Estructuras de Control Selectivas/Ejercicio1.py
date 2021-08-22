"""
Entradas
Capital-->float—>c
Intereses-->float-->i
Salidas
Total_capital-->int-->t
"""
c=float(input("Ingrese el capital que tiene: "))
i=float(input("Ingrese el porcentaje de intereses: "))
#caja negra
a=(c*i)/100
if(a>100_000):
  b=a+c
elif(a<100_000):
  b=c
#Salidas
print("Su dinero total es de: $","{:.0f}".format (b))