"""
Entradas
Presupuesto-->int-->a
Salidas
Ginecologia-->int-->G
Traumatologia-->int-->T
Pediatria-->int-->P
"""
a=int(input("Digite el presupuesto: "))
#caja negra
G=a*0.4
T=a*0.3
P=a*0.3
#Salidas
print("Ginecologia: $","{:.0f}".format(G))
print("Traumatologia: $","{:.0f}".format(T))
print("Pediatria: $","{:.0f}".format(P))
