"""
Entradas

Salidas
Suma-->int-->s
"""
s=0
for a in range(97,1004):
  if (a%2==0):
    s+=a
print(s)