tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
tabMeteo3 = [((2022,1,20), 2, 16, 0.1), ((2022,1,21), 1, 13, 0.2), ((2022,1,23), 6, 19, 0.6), ((2022,1,24), 3, 18, 0.8),((2022,2,20), 6, 19, 0.2), ((2022,2,24), 3, 18, 0.2), ((2022,2,28), 3, 18, 0.2)]

def medias(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        media = (tmin + tmax)/2
        res.append(data, media)

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for data, tmin, tmax, prec in t:
        ano, mes, dia = data
        f.write(f"{ano}-{mes}-{dia};{tmin};{tmax};{prec}\n")
    f.close()
    return

guardaTabMeteo(tabMeteo1, "meteorologia.txt")

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome, "r")
    for line in f:
        #line = line[:-1]
        line = line.strip()
        campos = line.split(";")
        data, tmin, tmax, prec = campos
        ano,mes, dia = data.split("-")
        tuplo = ((int(ano),int(mes),int(dia)),float(tmin),float(tmax),float(prec))
        res.append(tuplo)
    f.close()
    return res

tabMeteo2 = carregaTabMeteo("meteorologia.txt")

def minMin(tabMeteo):
    x = 100
    for data, tmin, tmax, prec in tabMeteo:
        if tmin < x:
            x = tmin
    return x

def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        ampl = tmax - tmin
        tuplo = (data, ampl)
        res.append(tuplo)
    return res 

def maxChuva(tabMeteo):
    max_prec = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec > max_prec:
            max_prec = prec
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append(data)
    return res

def maxPeriodoCalor(tabMeteo, p):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            res.append(data)
    return 

import matplotlib.pyplot as plt

def grafTabMeteo(t):
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data,tmin,tmax,prec in t]
    ytmin = [tmin for data,tmin,tmax,prec in t]
    ytmax = [tmax for data,tmin,tmax,prec in t]
    yprec = [prec for *_, prec in t]

    plt.plot(x,ytmin, label = "Temp. Minima (ºC)", marker = "D", color = "blue")
    plt.plot(x,ytmax, label = "Temp. Maxima (ºC)", marker = "d", color = "red")
    plt.legend()
    plt.xticks(rotation=45)
    plt.title("Tabela Meteorológica")
    plt.grid()
    plt.show()

    plt.bar(x,yprec, label = "Pluviosidade (mm)", marker = "o", color = "cyan")
    plt.xticks(rotation=45)
    plt.show()
    return

def menu():
    print("App de Análise Meteorológica")
    print(f"""""Os dados da lista tabMeteo3 estão carregados! Estes são:
           {tabMeteo3}""")
    print("1 - Carregar dados meteorológicos de um ficheiro")
    print("2 - Guardar dados meteorológicos para um ficheiro")
    print("3 - Média das temperaturas")
    print("4 - Temperatura mínima da lista")
    print("5 - Amplitude térmica diária")
    print("6 - Dia com maior pluviosidade")
    print("7 - Dias com pluviosidade acima de um valor")
    print("8 - Maior período de dias com pluviosidade abaixo de um valor")
    print("9 - Gráfico dos dados meteorológicos")
    print("0 - Sair")
    
    opcao=int(input("Escolha uma opção: "))
    if opcao==1:
        fnome = input("Nome do ficheiro: ")
        tabMeteo = carregaTabMeteo(fnome)
        print("Lista carregada")  
    elif opcao==2:
        fnome = input("Nome do ficheiro: ")
        guardaTabMeteo(tabMeteo, fnome)
        print("Lista guardada")
    elif opcao==3:
        medias(tabMeteo3)
        print(medias(tabMeteo3))
    elif opcao==4:
        print(minMin(tabMeteo3))
    elif opcao==5:
        print(amplTerm(tabMeteo3))
    elif opcao==6:  
        print(maxChuva(tabMeteo3))
    elif opcao==7:
        p = float(input("Valor de pluviosidade (mm): "))
        print(diasChuvosos(tabMeteo3, p))
    elif opcao==8:  
        p = float(input("Valor de pluviosidade (mm): "))
        print(maxPeriodoCalor(tabMeteo3, p))
    elif opcao==9:  
        grafTabMeteo(tabMeteo3)
    elif opcao==0:
        print("Adeus!")
    return

menu()