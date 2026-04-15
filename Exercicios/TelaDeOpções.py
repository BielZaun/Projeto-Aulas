# bibiliotecas utilizadas:
from datetime import datetime
from random import randint
from math import sqrt

#funções
def menu(opcao):
    if opcao == '1':
        return f'Numero Aleatorio: {randint(0, 100)}'

    elif opcao == '2':
        num = float(input('Digite um número: '))
        return sqrt(num)

    elif opcao == '3':
        return datetime.now().strftime('%d/%m/%Y')

    else:
        return 'Opção inválida, digite apenas \n[1][2][3]'

#Entrada de dados do usuario
while True:
    print('===== Menu de opções =====')
    print('[1] Numero aleatorio')
    print('[2] Raiz Quadrada')
    print('[3] Data Atual')

    ops = input('Qual opção deseja? ')

    resultado = menu(ops)

    print(resultado)

    continuar = input('Deseja continuar? [S/N] ').upper()

    if continuar != 'N' and continuar != 'S':
        print('Somente [S/N]')
        continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        print('---FIM---')
        break;