c = 1
n3 = 0
print('---------TABUADA---------')
n = int(input('Qual valor da multiplicação? '))
n2 = int(input('Em quantas x? '))
for c in range(1, n2+1):
    c *= n
    n3 += 1
    print(f'{n3} x {n} = {c}')
