fosforos=21
print("Jogo dos Fósforos:")
print("De 21 fósforos podes tirar entre 1 a 4 fósforos, quem o último fósforo tirar, perde o jogo")
input("Clique em Enter para começar: ")
jogador=int(input("Selecione 1 para ser o Jogador_1 ou 2 para ser o Jogador_2. O computador será o outro jogador: "))
if jogador==1:
    print("és o jogador_1")
    while fosforos>1:
        jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
        fosforos=fosforos-jogada
        print(f"restam {fosforos} fosforos")
        computador=5-jogada
        print(f"o computador tirou {computador} fósforos")
        fosforos=fosforos-computador
        print(f"restam {fosforos} fosforos")
        if fosforos<=1:
            print("tens de tirar o último fósforo")
            print("perdeste :(")
else:
    print("és o jogador_2 ")
    computador=1
    print(f"o computador tirou {computador} fósforos")
    fosforos=fosforos-computador
    print(f"restam {fosforos} fosforos")
    jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
    fosforos=fosforos-jogada
    print(f"restam {fosforos} fosforos")
    while fosforos>1:
        if jogada==5-computador:
            computador=1
            print(f"o computador tirou {computador} fósforos")
            fosforos=fosforos-computador
            print(f"restam {fosforos} fosforos")
            jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
            fosforos=fosforos-jogada
            print(f"restam {fosforos} fosforos")
            if fosforos<=1:
                print("resta 1 fósforo")
                print("ganhaste :)")
        else:
            computador=4-jogada
            print(f"o computador tirou {computador} fósforos")
            fosforos=fosforos-computador
            print(f"restam {fosforos} fosforos")
            jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
            fosforos=fosforos-jogada
            print(f"restam {fosforos} fosforos")
            computador=5-jogada
            print(f"o computador tirou {computador} fósforos")
            fosforos=fosforos-computador
            print(f"restam {fosforos} fosforos")
            jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
            fosforos=fosforos-jogada
            print(f"restam {fosforos} fosforos")
            computador=5-jogada
            print(f"o computador tirou {computador} fósforos")
            fosforos=fosforos-computador
            print(f"restam {fosforos} fosforos")
            jogada=int(input("selecione quantos fósforos pretende tirar (1,2,3 ou 4): "))
            fosforos=fosforos-jogada
            print(f"restam {fosforos} fosforos")
            computador=5-jogada
            print(f"o computador tirou {computador} fósforos")
            if fosforos<=1:
                print("tens de tirar o último fósforo")
                print("perdeste :(")