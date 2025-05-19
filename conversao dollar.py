print('escolha uma opcao:')
print('1- dolar para real:')
print('2-realpara dollar')

opcao=int(input('digite a opcao:'))
valor=float(input('informe a cotacao atrual do dolar:'))

if opcao ==1:
    dolares=float(input('informe a quantidade de dolar;'))
    print(f'o valor em reais é r${valor*dolares}')
elif opcao ==2:
    reais= float(input('informe a quantidades de reais:'))
    print(f' o valor em dolares ${reais/valor}')

else:
    print('opcao errada.')

      