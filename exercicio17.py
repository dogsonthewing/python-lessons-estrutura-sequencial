import math

tamanhoparede = float(input("digite "))
precolata = 80
precogalao = 25

litros = tamanhoparede 6
latas = math.ceil(litros / 18)
galoes = math.ceil(float(litros / 3.6))

def calc(tinta):
    menoslatas = math.floor(tinta / 18)
    if menoslatas < 1 :
        menoslatas = 1
    faltalitros = math.floor(tinta - (menoslatas * 18))
    maisgaloes = math.ceil(faltalitros / 3.6)
    return menoslatas , maisgaloes

print(latas , 'latas' , 'por R$' + str(precolata * latas))
print(galoes , 'Galões' , 'por R$' + str(precogalao * galoes))

lista = calc(litros)
print(lista[0],'latas e' , lista[1] , 'galões por R$' + str((precolata * lista[0])+(precogalao * lista[1])))
