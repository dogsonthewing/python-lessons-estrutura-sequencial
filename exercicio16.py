import math

tamanhoparede = int(input("digite "))
precolata = 80

litros = tamanhoparede / 3
latas = math.ceil(litros / 18)

print(latas , 'latas' , 'por R$' + str(precolata * latas))
