nome=input('nome do produto')
preço_original=float(input('valor original'))
porcentagem=float(input('porcentagem de desconto'))
desconto= preço_original* (porcentagem /100)
valor_novo = preço_original - porcentagem 
print('o',nome,'com',porcentagem,'de desconto ficou:',valor_novo)
print(f'o {nome}com {porcentagem}%de desconto de desconto custara:r${valor_novo}')