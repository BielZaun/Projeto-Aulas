valores = []

def inserir(valor):
    x = int(input('Digite um valor: '))
    valor.append(x)
    return valor

def valor(val):
    return f'Valore(s) Cadastrados: {val}'

def ordernar(lista):
    print('[1] Crescente')
    print('[2] Decrescente')
    op = input('Escolha: ')
    if op == '1':
        res = sorted(lista)
        return res
    elif op == '2':
        res2 = sorted(lista, reverse=True)
        return res2
    else:
        return 'Invalido'

def buscar(valor):
    w = int(input('Digite um valor: '))

    if w in valor:
        print('Esse valor existe!')
        print(f'Ele aparece {valor.count(w)} Vez(es)!')
    else:
        print('Valor não existe!')

    return valor

while True:
    print('--=--MENU--=--')
    print('[1] Cadastrar numero')
    print('[2] Valores cadastrados')
    print('[3] Analise dos numeros')
    print('[4] Mostrar ordem dos numeros')
    print('[5] Buscar numero na lista')
    print('[6] Sair')
    ops = input('Escolha uma opção: ')

    if ops == '1':
        print(inserir(valores))
    elif ops == '2':
        print(valor(valores))
    elif ops == '3':
        print(f'Quantidade de valores: {len(valores)}')
        print(f'Soma: {sum(valores)}')
        print(f'Média: {sum(valores) / len(valores):.2f}')
        print(f'Maior: {max(valores)}')
        print(f'Menor: {min(valores)}')

        par = 0
        impar = 0
        for i in valores:
            if i % 2 == 0:
                par += 1
            else:
                impar += 1

        print(f'Quantidade de numeros Pares: {par}')
        print(f'Quantidade de numeros impares: {impar}')

    elif ops == '4':
        print(ordernar(valores))
    elif ops == '5':
        print(buscar(valores))
    elif ops == '6':
        print('Finalizando....')
        break
    else:
        print('Opção invalida!!')
        continue