notaf1 = float(input('Digite a nota A1: '))
notaf2 = float(input('Digite a nota A2: '))
freq = int(input('Digite a frequencia: '))

nf = notaf1 + notaf2

if nf >= 6 and freq >= 75:
  print('Aprovado')
elif nf <= 6 and freq >= 75:
  print("Recuperação!")
  af = float(input('Digite a nota AF: '))
  if nf > notaf1:
    nf = af + notaf2
  if nf > notaf2:
    nf = af + notaf1
  if nf >= 6 and freq >= 75:
    print("Aprovado")
  else:
    print('Reprovado')
elif freq <= 75:
  print('Reprovado')
else:
  print('ERROR')
