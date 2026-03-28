n1 = float(input('Digite seu primeiro numero: '))
n2 = float(input('Digite seu seu segundo numero numero: '))
x = input('Qual operador você irá utilizar? (+, -, *, /, % ou **) ')

if x == '+':
  print(f'{n1} + {n2} = {n1 + n2:0.2f}')
elif x == '-':
  print(f'{n1} - {n2} = {n1 + n2:0.2f}')
elif x == '*':
  print(f'{n1} x {n2} = {n1 + n2:0.2f}')
elif x == '/':
  print(f'{n1} / {n2} = {n1 + n2:0.2f}')
elif x == '%':
  print(f'{n1} % {n2} = {n1 + n2:0.2f}')
elif x == '**':
  print(f'{n1} ** {n2} = {n1 + n2:0.2f}')
else:
  print('ERRO, digite corretamente o operador! ')