"""
Entradas
Monto_cuenta-->float->a
Nombre—>int—>n
Salidas
Cliente—>int—>n
Total_compra—>float—>a
Descuento-->float—>d
Total_pago—>float—>e
"""
n=input("Ingrese su nombre: ")
a=float(input("Ingrese el monto de la cuenta: "))
if(a<50_000):
  d=0
  e=a
elif(a>=50_000 and a<100_000):
  d=a*0.05
  e=a-d
elif(a>=100_000 and a<700_000):
  d=a*0.11
  e=a-d
elif(a>=700_000 and a<1_500_000):
  d=a*0.18
  e=a-d
elif(a>1_500_000):
  d=a*0.25
  e=a-d
print("Cliente: "+str(n))
print("Total de la compra: $","{:.0f}"
.format(a))
print("El descuento es de: $","{:.0f}"
.format(d))
print("El total a pagar es $","{:.0f}"
.format(e))