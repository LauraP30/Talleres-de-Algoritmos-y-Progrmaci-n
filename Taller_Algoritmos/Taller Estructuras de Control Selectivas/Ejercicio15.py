"""
Entradas
Nivel_Hemoglobina-->int-->n
Edad-->int-->e
Sexo-->int-->s
Salidas
Resultado-->str-->r
"""
n=int(input("Ingrese el nivel de hemoglobina: "))
e=int(input("Ingrese su edad en meses: "))
s=int(input("Si es mujer ingrese 1 y si es hombre ingrese 2: "))
if(e>=0 and e<=1):
  if(n>=13 and n<=26):
    r="Negativo"
  elif(n<13):
    r="Positivo"
elif(e>1 and e<=6):
  if(n>=10 and n<=18):
    r="Negativo"
  elif(e<10):
    r="Positivo"
elif(e>6 and e<=12):
  if(n>=11 and n<=15):
    r="Negativo"
  elif(n<11):
    r="Positivo"
elif(e>12 and e<=60):
  if(n>=11.5 and n<=15):
    r="Negativo"
  elif(n<11.5):
    r="Positivo"
elif(e>60 and e<=120):
  if(n>=12.6 and n<=15.5):
    r="Negativo"
  elif(n<12.6):
    r="Positivo"
elif(e>120 and e<=180):
  if(n>=13 and n<=16):
    r="Negativo"
  elif(n<13):
    r="Positivo"
if(s==1):
  if(e>180):
    if(n>=12 and n<=16):
      r="Negativo"
    elif(n<12):
      r="Positivo"
elif(s==2):
  if(e>180):
    if(n>=14 and n<=18):
      r="Negativo"
    elif(n<14):
      r="Positivo"
print("Su resultado es: "+str(r))