# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO ------------------------------------------
preco=float(input('qual e o preco do produto'))
porcentagem=float(input('digite o valor da porcentagem'))
desconto=porcentagem * (porcentagem / 100) 
print(f'o produto que custa r${preco:2f} tera r${desconto:.2f} de desconto.')