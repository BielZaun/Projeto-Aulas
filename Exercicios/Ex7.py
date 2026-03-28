idade = int(input('Qual sua idade? '))
doc = input('Possui documento ? (sim ou nao) ')
membro = input('Tem algum membro faltando? (sim ou nao) ')
alt = float(input('Qual sua altura? '))
gen = input('Você é homem ? (sim ou nao) ')
pres = input('Você é o presidente? (sim ou nao) ')

if (not(alt >= 1.80 and gen == 'sim') and idade >= 18 and doc == 'sim' and membro == 'nao') or pres == 'sim':
  print('Pode entrar')
else:
  print('Não pode entrar')