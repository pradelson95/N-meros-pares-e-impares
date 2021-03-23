from time import*

x = int(input("Desde que número: "))

y = int(input("Hasta que número: "))

while True:
 for numeros in range(x,y):
  if numeros%2==0:
    print(numeros,"es par de los numeros entre ",x,"y",y)
    sleep(1)
  
  else:
    print(numeros,"es impar de los numeros entre",x,"y",y)
    sleep(1)
    