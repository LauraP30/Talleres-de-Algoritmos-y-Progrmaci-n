a=0
g=0
d=0
while True:
  num=int(input())
  if(num==1):
    a=a+1
  elif(num==2):
    g=g+1
  elif(num==3):
    d=d+1
  elif(num==4):
    break
  else:
    continue
print("MUITO OBRIGADO")
print("Alcool: ",(a))
print("Gasolina: ",(g))
print("Diesel: ",(d))