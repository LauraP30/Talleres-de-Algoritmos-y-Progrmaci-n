"""
Entradas
Km-->int-->a
Salidas
Pago-->int-->b
"""
a=int(input("Ingrese los km: "))
if(a<300):
  b=50_000
elif(a>300):
  if(a<1_000):
    b=70_000+((a-300)*30_000)
  elif(a>1_000):
    b=150_000+((a-1000)*9_000)
print("Debe pagar: $","{:.0f}".format (b))