"""
Entradas
Sueldo-->float—>s
Salidas
Nuevo_Sueldo-->float->c
"""
s=float(input("Ingrese el sueldo: "))
if(s<900_000):
  c=(s*0.15)+s
elif(s>900_000):
  c=(s*0.12)+s
#Salidas
print("Su nuevo sueldo es de $","{:.0f}".format(c))