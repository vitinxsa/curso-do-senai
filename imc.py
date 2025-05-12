nome = input ('nome do aluno') 
altura = float (input('altura do aluno'))
peso = float (input('peso do aluno'))
IMC = peso / (altura * altura)

resultado = round(IMC, 2)

print(resultado)