"""
Entradas
Sueldo-->int-->s
Horas-->int-->h
Extras-->int-->ex
Salidas
Asignaciones-->int-->A
Deducciones-->int-->E
Neto-->int-->I
"""
s=int(input("Ingrese el salario: "))
h=int(input("Ingrese las horas trabajadas: "))
extras=int(input("Ingrese las horas extras: "))
#caja negra
a=250000
b=173000
c=180000
d=a+b+c
e=s*0.05
f=s*0.02
g=s*0.07
h=e+f+g
i=(1*s)/144
j=(25*i)/100
k=j*extras
l=s+d+k-h
#Salidas
print("Las asignaciones tienen un valor de: $","{:.0f}".format(d))
print("Las deducciones tienen un valor de: $","{:.0f}".format(h))
print("El sueldo neto es: $","{:.0f}".format(l))
