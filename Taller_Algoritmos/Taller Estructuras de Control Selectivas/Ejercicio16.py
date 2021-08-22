"""
Entradas
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
Salidas
X1-->int-->X1
X2-->int-->X2
"""
f=input().split(" ")
A,B,C,D=f
A=int(A)
B=int(B)
C=int(C)
D=B**2-4*A*C
import math
if(D==0):
  a=-B/(2*A)
  X1=a
  X2=a
elif(D>0):
  X1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
  X2=(-B+math.sqrt(B**2-4*A*C))/(2*A)
elif(D<0):
  X1="No tiene solucion"
  X2="No tiene solucion"
print("X1 vale: "+str(X1))
print("X2 vale: "+str(X2))