# Aluguel de carros:

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado


#(dias) Pedir a quantidade de dias
#(km) Pedir a quantidade de km percorridos
#(valor_dias) Calcular o valor total dos dias (dias * 60)
#(valor_km) Calcular o valor total da quilometragem (km * 0.15)
#(valor_total) Calcular o valor total somando o valor dos dias + o valor dos km
#Mostrar na tela a frase formatada
nome=input('nome_do_veiculo')
dias=int(input ('quantidadess de dias'))
km=float(input('km_percorridos'))
if nome=='992':
    valor_dias=int(dias*60)
    valor_km=(km*0.99)
    valor_total=(valor_dias+valor_km)
elif nome=='gtr':
    valor_dias=int(dias*31)
    valor_km=(km*0.99)
    valor_total=(valor_dias+valor_km)
print(valor_total) 