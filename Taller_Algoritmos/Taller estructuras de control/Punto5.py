"""
Entradas
Parciales-->int-->p
Examen-->int-->d
Trabajo-->int-->e
Salidas
Final-->int-->cf
"""
p=input("Notas de los parciales: ").split(" ")
a,b,c=p
a=int(a)
b=int(b)
c=int(c)
d=int(input("Nota del examen final: "))
e=int(input("Nota dle trabajo final: "))
#caja negra
np=(a+b+c)/3
F=np*0.55
E=d*0.3
G=e*0.15
cf=F+E+G
#Salidas
print("La nota final es: ","{:.1f}".format(cf))
