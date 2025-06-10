# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome=(input('digite o nome do produto'))
preco=float(input('digite o preco do produto'))
valor_desconto=float(input('digite o desconto do produto'))
desconto=preco*(valor_desconto/100)
print(desconto)
