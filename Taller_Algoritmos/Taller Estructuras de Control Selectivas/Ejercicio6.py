"""
Entradas
a-->int-->A
b-->int-->B
c-->int-->C
d-->int-->D
Salidas
Resultado-->int-->N
"""
x=input().split(" ")
A,B,C,D=x
A=int(A)
B=int(B)
C=int(C)
D=int(D)
#caja negra
e=A*1000
f=B*100
g=C*10
h=D*1
N=e+f+g+h
#Metodo round()
print(round(N,-2))