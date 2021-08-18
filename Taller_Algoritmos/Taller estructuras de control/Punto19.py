"""
Entradas
Naranjas-->int-->a
Docena-->int-->b
Ganancia-->int-->c
Salidas
Ganancia-->int-->G
"""
a=int(input("Digite el lote de naranjas: "))
b=int(input("Digite las docenas: "))
c=int(input("Digite las ganancias: "))
d=a/b
e=a+d
G=(100*c)/e
#Salidas
print("Su ganancia es de: ","{:.0f}%".format(G))
