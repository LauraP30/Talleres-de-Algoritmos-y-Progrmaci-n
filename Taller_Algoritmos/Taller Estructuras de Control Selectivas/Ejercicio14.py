"""
Entradas
Lectura_anterior-->int-->lan
Lectura_actual-->int-->lac
Salidas
Total_capital-->int-->t
"""
lan=int(input("Ingrese la lectura anterior: "))
lac=int(input("Ingrese la lectura actual: "))
#caja negra
a=lac-lan
if(a>=0 and a<=100):
  t=4_600
elif(a>=101 and a<=300):
  t=80_000
elif(a>=301 and a<=500):
  t=100_000
elif(a>=501):
  t=120_000
print("El total a pagar es: $","{:.0f}".format(t))