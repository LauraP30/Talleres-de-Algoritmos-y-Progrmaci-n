"""
Entradas
Cantidad-->float-->c
Salidas
Cien_mil-->float-->B1
Cincuenta_mil-->float-->B2
Veinte_mil-->float-->B3
Diez_mil-->float-->B4
Cinco_mil-->float-->B5
Dos_mil-->float-->B6
Mil-->float-->B7
Quinientos-->float-->M1
Doscientos-->float-->M2
Cien-->float-->M3
Cincuenta-->float-->M4
"""
c=int(input("Ingrese la cantidad de dinero: "))
if(c>=1000000):
  B1=c//100000
  print("Los billetes de 100000 COP son: "+str(B1))
  c=(c%100000)
if(c>=500000):
  B2=c//50000
  print("Los billetes de 50000 COP son: "+str(B2))
  c=c%50000
if(c>=20000):
  B3=c//20000
  print("Los billetes de 20000 COP son: "+str(B3))
  c=c%20000
if(c>=10000):
  B4=c//10000
  print("Los billetes de 10000 COP son: "+str(B4))
  c=c%10000
if(c>=5000):
  B5=c//5000
  print("Los billetes de 5000 COP son: "+str(B5))
  c=c%5000
if(c>=2000):
  B6=c//2000
  print("Los billetes de 2000 COP son: "+str(B6))
  c=c%2000
if(c>=1000):
  B7=c//1000
  print("Los billetes de 1000 COP son: "+str(B7))
  c=c%1000
if(c>500):
  M1=c//500
  print("Las monedas de 500 COP son: "+str(M1))
  c=c%500
if(c>=200):
  M2=c//200
  print("Las monedas de 200 COP son: "+str(M2))
  c=c%200
if(c>=100):
  M3=c//100
  print("Las monedas de 100 COP son: "+str(M3))
  c=c%100
if(c>=50):
  M4=c//50
  print("Las monedas de 50 COP son: "+str(M4))
  c=c%50