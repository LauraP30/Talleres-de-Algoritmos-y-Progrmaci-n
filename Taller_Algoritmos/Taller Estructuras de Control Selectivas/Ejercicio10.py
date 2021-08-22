"""
Entradas
Sueldo_bruto-->float-->sa
Salidas
Categoria-->int-->c
Sueldo_neto-->float-->sn
"""
sa=float(input("Digite el salario bruto: "))
sn=0.0#float
if(sa>=5_000_000):
  sn=(sa*0.10)+sa
  c=1
elif(sa<5_000_000 and sa>=4_300_000):
  sn=(sa*0.15)+sa
  c=2
elif(sa<4_300_000 and sa>=3_600_000):
  sn=(sa*0.20)+sa
  c=3
elif(sa<3_600_000 and sa>=2_000_000):
  sn=(sa*0.40)+sa
  c=4
elif(sa<2_000_000 and sa>=900_000):
  sn=(sa*0.60)+sa
  c=5
print("La categoria es: "+str(c))
print("El sueldo neto es de: $","{:.0f}".format(sn))