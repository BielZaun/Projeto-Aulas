lista = []


def apagar():
  x = input('Deseja limpar a lista? [s/n] ').upper()
  if x == 'S':
    lista.clear()
    print('Lista apagada')
    print(lista)
  elif x == 'N':
    print('Lista mantida')
  else:
    print('Invalido')



def adicionar(list):
  while True:
    adc = int(input('Adicione um numero: '))
    lista.append(adc)
    n = input('Deseja continuar adicionando? [S/N] ').upper()
    if n == 'S':
      continue
    elif n == 'N':
      break
    else:
      print('Comando invalido')


def remover(list):
  while True:
    print(lista)
    num = int(input('Qual numero remover? '))

    if num in lista:
      real = input('Deseja realmente remover? ([S/N])').upper()
      if real == 'S':
        lista.remove(num)
      else:
        continue
    else:
      print('Numero inexistente!')

while True:
  print('--=-MENU-=---')
  print('[1] Apagar lista')
  print('[2] Adicionar numeros')
  print('[3] Exibir lista')
  print('[4] Analisar lista')
  print('[5] Remover numero da lista')
  print('[6] Finalizar o programa')

  ops = input('Qual opção deseja? ')

  if ops == '1':
    apagar()
  elif ops == '2':
    adicionar(lista)
  elif ops == '3':
    print(lista)
  elif ops == '4':
    impar = 0
    par = 0

    print(f'Quantidade de numero(s): {len(lista)}')
    for i in lista:
      if i % 2 == 0:
        par += 1
      else:
        impar +=1
    print(f'Quantidade de numeros impar(es): {impar}')
    print(f'Quantidade de numeros par(es): {par}')

    positivo = 0
    negativo = 0
    nulos = 0

    for i in lista:
      if i > 0:
        positivo += 1
      elif i < 0:
        negativo += 1
      else:
        nulos =+ 1
    print(f'Quantidade de positivos: {positivo}')
    print(f'Quantidade de negativos: {negativo}')
    print(f'Quantidade de Nulos: {nulos}')
    print(f'Maior numero {max(lista)}')
    print(f'Menor numero {min(lista)}')
    print(f'Média {sum(lista) / len(lista):.2f}')
  elif ops == '5':
    remover(lista)
  elif ops == '6':
    sair = input('REALMENTE quer finalizar? [S/N] ').upper()
    if sair == 'S':
      print('Finalizando...')
      break
    elif sair == 'N':
      continue
    else:
      print('Comando invalido!')