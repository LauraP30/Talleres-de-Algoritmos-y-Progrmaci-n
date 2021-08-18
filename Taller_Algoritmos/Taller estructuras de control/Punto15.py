"""
Entradas
Final-->int-->f
Venta-->int-->v
Salidas
Descuento-->int-->d
"""
f=int(input("Ingrese el valor final: "))
v=int(input("Ingrese el valor de la venta: "))
#caja negra
a=v-f
b=(a*100/v)
#Salidas
print("El descuento que se aplico fue: ","{:.0f}%".format(b))
