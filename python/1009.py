vendedor = input("")
salario_fixo = float(input())
vendas_mes = float(input())
salario = ( 15/100 * vendas_mes) + salario_fixo
print('TOTAL = R$ {:.2f}'.format(salario))