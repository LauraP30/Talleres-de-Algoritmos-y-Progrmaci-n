"""
Entradas

Salidas
Doceavo-->int-->b
Suma-->int-->c
"""
b=0
for a in range(1,13):
  if(a>=1):
    b=5*a+1
    if(b==61):
      c=(b+6)*6
      print("a12: "+str(b))
      print("suma: "+str(c))
  elif(a==13):
    break