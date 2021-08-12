desconto_imposto = 0.89 
desconto_inss = 0.92
desconto_sindicato = 0.95
#multiplique para aplicar os descontos


valor_hora = int(input("Digite o valor da sua hora trabalhada: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
print('---------------------------------------------------------')

salario_bruto = valor_hora * horas_trabalhadas
desconto_imposto = salario_bruto - (desconto_imposto * salario_bruto)
desconto_inss = salario_bruto - (desconto_inss * salario_bruto)
desconto_sindicato = salario_bruto - (desconto_sindicato * salario_bruto)
salario_liquido = salario_bruto - desconto_imposto - desconto_inss - desconto_sindicato

print('+ Salário Bruto : R$' , salario_bruto)
print('- IR (11%) : R$' , desconto_imposto)
print('- INSS (8%) : R$' , desconto_inss)
print('- Sindicato (5%) : R$' , desconto_sindicato)
print('= Salario Liquido : R$' , salario_liquido)