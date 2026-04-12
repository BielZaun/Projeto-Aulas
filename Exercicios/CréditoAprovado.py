import time
print('====Empréstimo para Casa====')

casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual é o seu salario? R$'))
tempo = int(input('Quantos anos você irá pagar? '))

meses = 12 * tempo
prest = casa / meses

porcent = (sal / 100) * 30

print('Processando...')
time.sleep(2)

if porcent >= prest:
    print('Parabéns, emprestimo aprovado!')
    print(f'Valores das parcelas ficou: R${meses:0.2f} em {meses}x')
else:
    print('Infelizmente o crédito não foi aprovado!')
    print('O valor excedeu 30% do seu salario! ')
    print(f'Valor das prestações: R${prest:.2f}')



