"""
Entradas
Salario-->float-->s
Ventas_1-->float-->v1
Ventas_2-->float-->v2
Ventas_3-->float-->v3
Salidas
Total_1-->float-->t1
Total_2-->float-->t2
Total_3-->float-->t3
"""
s=float(input("Ingrese su salario bruto: "))
v1=float(input("Ingrese las ventas del departamento 1: "))
v2=float(input("Ingrese las ventas del departamento 2: "))
v3=float(input("Ingrese las ventas del departamento 3: "))
vt=v1+v2+v3
p=vt*0.33
if(v1>p):
  t1=(s*0.20)+s
else:
  t1=s
if(v2>p):
  t2=(s*0.20)+s
else:
  t2=s
if(v3>p):
  t3=(s*0.20)+s
else:
  t3=s
print("El pago del departamento 1 es: $","{:.0f}".format(t1))
print("El pago del departamento 2 es: $","{:.0f}".format(t2))
print("EL pafo del departamento 3 es: $","{:.0f}".format(t3))