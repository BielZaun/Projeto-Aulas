lista = []

def adicionar(valor):
    x = int(input('Digite um valor: '))
    lista.append(x)

def remover(valor):
    print(lista)
    y = int(input('Qual valor deseja remover?: '))
    lista.remove(y)

def buscar(valor):
    z = int(input('Qual numero deseja buscar?: '))
    if z in lista:
        print('Este numero exite na lista! ')
        print(f'Ele aparece {lista.count(z)} vez(es) ')
        print(lista)
    elif len(lista) == 0:
        print('Não existe numero na lista')
    else:
        print('Valor inexistente!')


    return

def ordernar(lista):
    print('[1] Crescente')
    print('[2] Decrescente')
    p = input('Qual ordem deseja?: ')

    if p == '1':
        print(sorted(lista))
    elif p == '2':
        print(sorted(lista, reverse=True))
    else:
        print('Opção invalida')
    return



while True:
    print('--==--MENU--==--')
    print('[1] Inserir numero')
    print('[2] Remover numero')
    print('[3] Mostrar lista')
    print('[4] Analise da lista')
    print('[5] Buscar numero')
    print('[6] Ordernar lista')
    print('[7] Sair')
    ops = input('O que deseja? ')

    if ops == '1':
        adicionar(lista)
    elif ops == '2':
        remover(lista)
    elif ops == '3':
        print(lista)
    elif ops == '4':
        print(f'Existe {len(lista)} numeros na lista')
        print(f'Soma de todos os numeros: {sum(lista)}')
        print(f'Média da lista: {sum(lista) / len(lista):.2f}')
        print(f'Maior numero {max(lista)}')
        print(f'Menor numero {min(lista)}')

        par = 0
        impar = 0
        for i in lista:
            if i % 2 == 0:
                par += 1
            else:
                impar += 1
        print(f'Existe {par} par(es)')
        print(f'Existe {impar} impar(es)')

    elif ops == '5':
        buscar(lista)
    elif ops == '6':
        ordernar(lista)
    elif ops == '7':
        print('Finalizando....')
        break
    else:
        print('Opção invalida! ')
        continue



