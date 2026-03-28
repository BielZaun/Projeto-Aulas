import random
import time

print('JOGO DE ADIVINHAÇÃO')
x = int(input('Digite um numero entre 0 a 5: '))

pc = random.randint(0, 5)
print('Processando...')
time.sleep(2)
if x == pc:
    print(f'Acertou! \nPc: {pc} \nVocê {x}')
elif x > 5:
    print('De 0 a 5, não um numero maior!')
else:
    print(f'Perdeu! \nPc: {pc} \nVocê: {x} ')






