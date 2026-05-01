numeros = []

def cadastrar(lista):
    valor = int(input("Digite um número: "))
    lista.append(valor)
    print("Número adicionado!")
    return lista

def exibir(lista):
    print("Lista:", lista)
    return lista

def analise(lista):
    if len(lista) == 0:
        print("Lista vazia!")
        return

    quantidade = len(lista)
    soma = sum(lista)
    media = soma / quantidade
    maior = max(lista)
    menor = min(lista)

    pares = 0
    impares = 0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Quantidade:", quantidade)
    print("Soma:", soma)
    print("Média:", media)
    print("Maior:", maior)
    print("Menor:", menor)
    print("Pares:", pares)
    print("Ímpares:", impares)

    return quantidade, soma, media, maior, menor, pares, impares

def ordenar(lista):
    print("1 - Crescente")
    print("2 - Decrescente")
    op = input("Escolha: ")

    if op == "1":
        print("Ordem crescente:", sorted(lista))
        return sorted(lista)
    elif op == "2":
        print("Ordem decrescente:", sorted(lista, reverse=True))
        return sorted(lista, reverse=True)

def buscar(lista):
    valor = int(input("Digite o número para buscar: "))

    if valor in lista:
        vezes = lista.count(valor)
        print("O número existe na lista!")
        print("Aparece", vezes, "vez(es)")
        return vezes
    else:
        print("Número não encontrado.")
        return 0


while True:
    print("\n---==MENU== ---")
    print("[1] - Cadastrar número")
    print("[2] - Exibir lista")
    print("[3] - Análise")
    print("[4] - Ordenar")
    print("[5] - Buscar")
    print("[6] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar(numeros)
    elif opcao == "2":
        exibir(numeros)
    elif opcao == "3":
        analise(numeros)
    elif opcao == "4":
        ordenar(numeros)
    elif opcao == "5":
        buscar(numeros)
    elif opcao == "6":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")