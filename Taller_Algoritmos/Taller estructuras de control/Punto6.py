"""
Entradas
Hombres-->int-->a
Mujeres-->int-->b
Salidas
%h-->int-->h
%m-->int-->m
"""
a=int(input("Numero de hombres: "))
b=int(input("Numero de mujeres: "))
#caja negra
c=a+b
ph=(a/c)*100
pm=(b/c)*100
#Salidas
print("Hombres son el ","{:.0f}%".format(ph))
print("Mujeres son el ","{:.0f}%".format(pm))
