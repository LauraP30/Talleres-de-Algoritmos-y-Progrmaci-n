"""
Entradas
Tareasm-->int-->m
Examenm-->int-->em
Tareasf-->int-->f
Examenf-->int-->ef
Tareasq-->int-->q
Examenq-->int-->eq
Salidas
Promediom-->int-->B
Promediof-->int-->D
Promedioq-->int-->F
Promediot-->int-->P
"""
m=input("Tareas de matematicas: ").split(" ")
a,b,c=m
a=int(a)
b=int(b)
c=int(c)
em=int(input("Examen de matematicas: "))
f=input("Tareas de fisica: ").split(" ")
d,e=f
d=int(d)
e=int(e)
ef=int(input("Examen de fisica: "))
q=input("Tareas de quimica: ").split(" ")
g,h,i=q
g=int(g)
h=int(h)
i=int(i)
eq=int(input("Examen de quimica: "))
#caja negra
A=(a+b+c)/3
B=(A*0.1)+(em*0.9)
C=(d+e)/2
D=(C*0.2)+(ef*0.8)
E=(g+h+i)/3
F=(E*0.15)+(eq*0.85)
P=(B+D+F)/3
#Salidas
print("Promedio matematicas: ","{:.1f}".format(B))
print("Prmedio fisica: ""{:.1f}".format(D))
print("Promedio quimica: ""{:.1f}".format(F))
print("Promedio total: ""{:.1f}".format(P))
