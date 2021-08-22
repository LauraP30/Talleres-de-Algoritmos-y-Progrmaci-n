"""
Entradas
Temperatura-->float-->t
Salidas
Deporte-->str-->d
"""
t=float(input("Ingrese la temperatura: "))
d=""#str
if(t>85):
  d="Natacion"
elif(t>70 and t<=85):
  d="Tenis"
elif(t>32 and t<=70):
  d="Golf"
elif(t>10 and t<=32):
  d="Esqui"
elif(t<=10):
  d="Marcha"
print("El deporte que puede practicar es: "+str(d))