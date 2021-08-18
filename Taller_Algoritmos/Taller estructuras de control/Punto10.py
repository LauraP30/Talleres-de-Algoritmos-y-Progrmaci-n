"""
Entradas
ChelinesA-->int-->CA
DracmasG-->int-->DG
Pe-->int-->P
Salidas
Pe-->int-->A
Fr-->int-->C
Do-->int-->D
Li-->int-->E
"""
CA=int(input("Digite los chelines austriaco: "))
DG=int(input("Digite los dracmas griegos: "))
P=int(input("Digite las pesetas: "))
#caja negra
A=(CA*956.871)/100
B=(DG*88.607)/1000
C=(B*1)/20.110
D=(P*1)/122.499
E=(P*100)/9.289
#Salidas
print("Chelines austriacos equivalen a: $","{:.0f}".format(A),"pesetas")
print("Dracmas griegos equivalen a: $","{:.0f}".format(C),"francos franceses")
print("Pesetas equivalen a: $","{:.0f}".format(D),"dolares EEUU")
print("Pesetas equivales a:  $","{:.0f}".format(E),"liras italianas")
