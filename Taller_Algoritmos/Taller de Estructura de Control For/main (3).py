archivo = open('paises.txt', 'r')

"""
#Imprima la posicion de Colombia
c=0
posicion=[]
for i in archivo:
  posicion.append(i)
  a=" ".join(posicion)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  posicion=[]   
print("Colombia se encuentra en la posición: ",(c))
"""


"""
#Imprima todos los Paises
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    paises.append(i[r])
  a="".join(paises)
  print(a)
  paises=[]
"""


"""
#Imprima todas las Capitales
capitales=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    capitales.append(i[r])
  a="".join(capitales)
  print(a.strip())
  capitales=[]
"""


"""
#Imprimir todos los Paises que inicien con la letra C
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""


"""
#Imprima todas las capitales que inicien con la leta B
lista=[]
capitales=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  capitales.append(a)
  lista=[]
for i in capitales:
  if(i[0]=="B"):
    print(i.strip())  
"""


"""
#Cuente e imprima cuantas ciudades inician con la letra M  
c=0
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i.strip()) 
for j in ciudad:
  if(j[0]=="M"):
    c=c+1
print("La cantidad de ciudades que empiezan con la letra M son: ",c)
"""


"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
lista=[]
lista2=[]
paises=[]
capitales=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista2.append(i[r])
  a="".join(lista2)
  capitales.append(a)
  lista2=[]
for i in paises:
  if(i[0]=="U"):
    print("Paises: ",i)
for i in capitales:
  if(i[0]=="U"):
    print("Capitales: ",i.strip())
"""


"""
#Cuente e imprima cuantos Países hay en el archivo
c=0
lista=[]
for i in archivo:
  c=c+1
print("El total de países es de: ",c)
"""


"""
#Busque e imprima la ciudad de Singapur
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    ciudad.append(i[r])
  a="".join(ciudad)
  if(a=="Singapur\n"):
    break
  ciudad=[]
print(a)
"""


"""
#Busque e imprima el País de Venezuela y su capital
pais=[]
for i in archivo:
  pais.append(i)
  a=" ".join(pais)
  if(a=="Venezuela: Caracas\n"):
    break
  pais=[]
print(a)
"""


"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
c=0
lista=[]
lista2=[]
ciudades=[] 
paises=[] 
for i in archivo:
  if(i[0]=="E"):
    a=i.index(":")
    for r in range(a+2,len(i)):
      lista.append(i[r])
    a="".join(lista)
    ciudades.append(a)
    lista=[]
for i in ciudades:
    for i in archivo:
      a=i.index(":")
      for r in range(a+2,len(i)):
        lista2.append(i[r])
      a="".join(lista2)
      ciudades.append(a)
      lista2=[]
    if(c==11):
      break
    c=c+1
    print(c, i.strip())
"""  


"""
#Busque e imprima la Capital de Colombia
capital=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    capital.append(i[r])
  a="".join(capital)
  if(a=="Bogotá\n"):
    break
  capital=[]
print(a)
"""


"""
#Imprima la posicion del pais de Uganda
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(c)
"""


"""
#Imprima la posicion del pais de Mexico
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="México\n"):
    break
  lista=[]   
print(c)
"""


"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato

pais=[]
for i in archivo:
  pais.append(i)
  a=" ".join(pais)
  if(a=="Madagascar: rey julien\n"):
    break
    for i in archivo:
      a=i.index(":")
    for r in range(a+2,len(i)):
      pais.append(i[r])
    a="".join(pais)
    pais.append(a)
    for i in pais:
      if(i=="rey julien"):
        pais.append(i)
        pais.pop(i)
        pais.append("Antananarivo")
    pais=[]
    print(pais)
"""


"""
#Agregue un país que no esté en la lista 
pais=[]
pais.append("Qatar\n")
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    pais.append(i[r])
  a="".join(pais)
  print(a)
  pais=[]
"""


archivo.close()