salario = float(input('Qual é o seu salario? '))

if salario >= 1250:
    x = (salario / 100) * 10
    salario = salario + x
    print(f'Teve um reajuste de 10%, seu novo salario R${salario:.2f}')
else:
    x = (salario / 100) * 15
    salario = salario + x
    print(f'Teve um reajuste de 15%, seu novo salario R${salario:.2f}')