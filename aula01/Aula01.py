import math as mt
listaRestos = []
num = int(input("Insira um numero: "))
num2 = int(0)
count = int(0)
while num > 1:
    num2 = mt.floor(num)
    listaRestos.append(num2%2)
    num = num/2
    count = count + 1

codigoBinario = listaRestos[::-1]

print("Esse numero em binário: ", end="")
for c in range(0,count):
    print(codigoBinario[c],end="")