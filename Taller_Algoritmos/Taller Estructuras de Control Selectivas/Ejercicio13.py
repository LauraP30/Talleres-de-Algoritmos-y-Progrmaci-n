"""
Entradas
Dia-->int-->d
Mes-->int-->m
Año-->int-->a
Salidas
Signo-->str-->s
Edad-->int-->e
"""
d=int(input("Ingrese el dia de nacimiento: "))
m=int(input("Ingrese el mes de nacimiento en numero: "))
a=int(input("Ingrese su año de nacimiento: "))
if((m==11) and (d>=22)) or ((m==12) and (d<=21)):
  s="Sagitario"
elif((m==12) and (d>=22)) or ((m==1) and (d<=20)):
  s="Capricornio"
elif((m==1) and (d>=21)) or ((m==2) and (d<=19)):
  s="Acuario"
elif((m==2) and (d>=20)) or ((m==3) and (d<=19)):
  s="Piscis"
elif((m==3) and (d>=21)) or ((m==5) and (d<=21)):
  s="Tauro"
elif((m==5) and (d>=22)) or ((m==6) and (d<=21)):
  s="Geminis"
elif((m==6) and (d>=22)) or ((m==7) and (d<=22)):
  s="Cancer"
elif((m==7) and (d>=23)) or ((m==8) and (d<=23)):
  s="Leo"
elif((m==8) and (d>=24)) or ((m==9) and (d<=22)):
  s="Virgo"
elif((m==9) and (d>=23)) or ((m==10) and (d<=22)):
  s="Libra"
elif((m==10) and (d>=23)) or ((m==11) and (d<=21)):
  s="Escorpion"
if((m==8) and (d>=24)) or ((m==9) and (d<=22)):
  e=2021-a-1
elif((m==9) and (d>=23)) or ((m==10) and (d<=22)):
  e=2021-a-1
elif((m==10) and (d>=23)) or ((m==11) and (d<=21)):
  e=2021-a-1
elif((m==11) and (d>=22)) or ((m==12) and (d<=21)):
  e=2021-a-1
elif((m==12) and (d>=22)) or ((m==1) and (d<=20)):
  e=2021-a-1
else:
  e=2021-a
print("Su signo es: "+str(s))
print("Su edad es: ","{:.0f}".format(e))