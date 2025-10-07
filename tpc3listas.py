import random

def menu():
    print("Manipulação de Listas de Inteiros")
    print("(1) Criar Lista (aleatória)")
    print("(2) Ler Lista (personalizada)")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) está Ordenada? (crescente)")
    print("(8) está Ordenada? (decrescente)")
    print("(9) Procura um elemento")
    print("(0) Sair")

def cria_lista_aleatoria(tamanho):
    if tamanho <= 0:
        return []
    lista = []
    i = 0
    while i < tamanho:
        lista.append(random.randint(1, 100))
        i = i + 1
    return lista

def ler_lista_personalizada(tamanho):
    lista = []
    i = 0
    while i < tamanho:
            valor = int(input(f"Introduz o elemento {i} (inteiro): "))
            lista.append(valor)
            i = i + 1
    return lista

def soma_lista(lista):
    if not  lista:
        return 0
    total = 0
    i = 0
    while i < len(lista):
        total += lista[i]
        i = i + 1
    return total

def media_lista(lista):
    if not lista:
        return None
    total = soma_lista(lista)
    return total / len(lista)

def maior_elemento(lista):
    if not lista:
        return None
    maior = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > maior:
            maior = lista[i]
        i = i + 1
    return maior

def menor_elemento(lista):
    if not lista:
        return None
    menor = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < menor:
            menor = lista[i]
        i = i + 1
    return menor

def esta_ordenada_crescente(lista):
    if len(lista) < 2:
        return True
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            return False
        i = i + 1
    return True

def esta_ordenada_decrescente(lista):
    if len(lista) < 2:
        return True
    i = 0
    while i < len(lista) - 1:
        if lista[i] < lista[i+1]:
            return False
        i = i + 1
    return True

def procura_elemento(lista, valor):
    i = 0
    while i < len(lista):
        if lista[i] == valor:
            return i
        i = i + 1
    return -1

def main():
    lista_atual = [] 
    while True:
        menu()
        opcao = input("Escolhe uma opção (número): ")
        if not opcao:
            print("Opção vazia. Tenta outra vez.") 

        if opcao == "1":
                n = int(input("Quantos elementos queres gerar? "))
                if n < 0:
                      print("Resposta inválida. Insira um valor n > 0.")
                if n >= 0:
                  lista_atual = cria_lista_aleatoria(n)
                  print("Nova lista criada:", lista_atual)

        elif opcao == "2":
                n = int(input("Quantos elementos queres introduzir? "))
                if n < 0:
                    print("Resposta inválida. Insira um valor n > 0.")
                if n >= 0:
                  lista_atual = ler_lista_personalizada(n)
                  print("Nova lista (do utilizador) criada:", lista_atual)

        elif opcao == "3":
            if not lista_atual:
                print("Lista vazia (não é possível fazer a soma)")
            else:
                s = soma_lista(lista_atual)
                print("Soma dos elementos:", s)

        elif opcao == "4":
            if not lista_atual:
                print("Lista vazia (não é possível efetuar a média)")
            else:
                m = media_lista(lista_atual)
                print("Média dos elementos:", m)

        elif opcao == "5":
            if not lista_atual:
                print("Lista vazia (não há elementos suficientes)")
            else:
                mx = maior_elemento(lista_atual)
                print("Maior elemento:", mx)

        elif opcao == "6":
            if not lista_atual:
                print("Lista vazia (não há elementos suficientes)")
            else:
                mn = menor_elemento(lista_atual)
                print("Menor elemento:", mn)

        elif opcao == "7":
            if esta_ordenada_crescente(lista_atual):
                print("A lista está ordenada por ordem crescente.")
            else:
                print("A lista não está ordenada por ordem crescente.")

        elif opcao == "8":
            if esta_ordenada_decrescente(lista_atual):
                print("A lista está ordenada por ordem decrescente.")
            else:
                print("A lista não está ordenada por ordem decrescente.")

        elif opcao == "9":
            if not lista_atual:
                print("Lista vazia (não há elementos suficientes)")
            else:
                  valor = int(input("Que valor queres procurar? "))
            procurado = procura_elemento(lista_atual, valor)
            print("Posição (0,...,n):", procurado)

        elif opcao == "0":
            print("Programa terminado. Lista final guardada:", lista_atual)
            break

        else:
            print("Opção inválida, tenta novamente")

main()