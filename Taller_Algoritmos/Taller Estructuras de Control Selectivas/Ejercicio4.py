"""
Entradas
Monto_total-->float-->m
Salidas
Fondos-->float-->a
Credito-->float-->d
Intereses-->float-->f
Prestamo-->float-->b
"""
m=float(input("Ingrese el valor total de la compra: "))
if(m>5_000_000):
  a=m*0.55
  b=m*0.3
  c=1-(0.55+0.3)
  d=m*c
  e=d*0.2
  f=d+e
elif(m<5_000_000):
  a=m*0.7
  b=0
  c=1-0.7
  d=m*c
  e=d*0.2
  f=d+e
print("La cantidad de fondos a invertir de la empresa es: $","{:.0f}".format(a))
print("La cantidad a pagar a credito es: $","{:.0f}".format(d))
print("El monto a pagar por intereses es de: $","{:.0f}".format(f))
print("El dinero prestado del banco es: $","{:.0f}".format(b))