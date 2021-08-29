"""
Entradas
k-->int-->k
n-->int-->n
Salidas
n-->int-->n
"""
n=0
k=int(input())
n=int(input())
while(k>=0 and n>=0):
  if(k<n):
    n=n-1
    print(n)
  elif(n<k):
    break