# solução para gráficos funcionais
import matplotlib
matplotlib.use("TkAgg")

import FreeSimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt


# Constantes
CHEGADA = "chegada"
SAIDA = "saida"

# =========================
# Funções auxiliares
# =========================
def gera_intervalo_tempo_chegada(lmbda):
    return np.random.exponential(1 / lmbda)

def gera_tempo_consulta(tempo_medio, distribuicao):
    if distribuicao == "exponential":
        return np.random.exponential(tempo_medio)
    elif distribuicao == "normal":
        return max(0, np.random.normal(tempo_medio, 5))
    elif distribuicao == "uniform":
        return np.random.uniform(tempo_medio * 0.5, tempo_medio * 1.5)

def procura_medico_livre(medicos):
    for m in medicos:
        if not m["ocupado"]:
            return m
    return None

def enqueue(q, e):
    q.append(e)
    q.sort(key=lambda x: x[0])
    return q

# =========================
# SIMULAÇÃO
# =========================
def simula(num_medicos, taxa_chegada, tempo_medio, distribuicao, tempo_simulacao, log):
    tempo_atual = 0.0
    queue_eventos = []

    fila_prioritaria = []
    fila_normal = []

    timeline = []
    tamanhos_fila = []
    tempos_espera = []  # (tempo_espera, instante)

    timeline_ocupacao = []
    ocupacao_medicos = []

    medicos = [
        {"id": f"m{i}", "ocupado": False, "doente": None,
         "inicio": 0.0, "tempo_ocupado": 0.0}
        for i in range(num_medicos)
    ]

    # Geração de chegadas
    contador = 1
    tempo_atual += gera_intervalo_tempo_chegada(taxa_chegada)
    while tempo_atual < tempo_simulacao:
        enqueue(queue_eventos, (tempo_atual, CHEGADA, f"d{contador}"))
        contador += 1
        tempo_atual += gera_intervalo_tempo_chegada(taxa_chegada)

    tempo_atual = 0.0
    doentes_atendidos = 0

    while queue_eventos:
        evento = queue_eventos.pop(0)
        tempo_atual = evento[0]

        # Promoção automática (>30 min)
        for d in fila_normal[:]:
            if tempo_atual - d[1] > 30:
                fila_normal.remove(d)
                fila_prioritaria.append(d)

        timeline.append(tempo_atual)
        tamanhos_fila.append(len(fila_prioritaria) + len(fila_normal))

        ocupados = sum(1 for m in medicos if m["ocupado"])
        timeline_ocupacao.append(tempo_atual)
        ocupacao_medicos.append(ocupados / num_medicos)

        if evento[1] == CHEGADA:
            medico = procura_medico_livre(medicos)
            if medico:
                medico["ocupado"] = True
                medico["doente"] = evento[2]
                medico["inicio"] = tempo_atual
                duracao = gera_tempo_consulta(tempo_medio, distribuicao)
                enqueue(queue_eventos, (tempo_atual + duracao, SAIDA, evento[2]))
                tempos_espera.append((0, tempo_atual))
            else:
                fila_normal.append((evento[2], tempo_atual))

        elif evento[1] == SAIDA:
            doentes_atendidos += 1
            medico = next(m for m in medicos if m["doente"] == evento[2])
            medico["ocupado"] = False
            medico["doente"] = None
            medico["tempo_ocupado"] += tempo_atual - medico["inicio"]

            if fila_prioritaria:
                prox, t_chegada = fila_prioritaria.pop(0)
            elif fila_normal:
                prox, t_chegada = fila_normal.pop(0)
            else:
                continue

            medico["ocupado"] = True
            medico["doente"] = prox
            medico["inicio"] = tempo_atual
            duracao = gera_tempo_consulta(tempo_medio, distribuicao)
            enqueue(queue_eventos, (tempo_atual + duracao, SAIDA, prox))
            tempos_espera.append((tempo_atual - t_chegada, tempo_atual))

    # =========================
    # Estatísticas
    # =========================
    esperas = [e for e, _ in tempos_espera]

    log(f"Doentes atendidos: {doentes_atendidos}")
    log(f"Tamanho médio da fila: {np.mean(tamanhos_fila):.2f}")
    log(f"Tamanho máximo da fila: {np.max(tamanhos_fila)}")

    if esperas:
        log(f"Tempo médio de espera: {np.mean(esperas):.2f} min")
        log(f"Tempo máximo de espera: {np.max(esperas):.2f} min")
        log(f"P50 espera: {np.percentile(esperas,50):.2f} min")
        log(f"P90 espera: {np.percentile(esperas,90):.2f} min")

    for m in medicos:
        log(f"{m['id']} ocupado {m['tempo_ocupado']/60:.2f} horas")

    return {
        "timeline": timeline,
        "fila": tamanhos_fila,
        "tempos_espera": tempos_espera,
        "timeline_ocupacao": timeline_ocupacao,
        "ocupacao": ocupacao_medicos
    }

# =========================
# Gráficos
# =========================
def gerar_graficos(res):
    plt.figure("Evolução da Fila")
    plt.step(res["timeline"], res["fila"], where="post")
    plt.xlabel("Tempo (min)")
    plt.ylabel("Nº doentes")
    plt.grid(True)

    # Evolução do tempo de espera
    if res["tempos_espera"]:
        tempos = [t for _, t in res["tempos_espera"]]
        esperas = [e for e, _ in res["tempos_espera"]]

        plt.figure("Evolução do Tempo de Espera")
        plt.plot(tempos, esperas, marker="o", linestyle="-")
        plt.xlabel("Tempo do turno (min)")
        plt.ylabel("Tempo de espera (min)")
        plt.grid(True)

    plt.figure("Ocupação dos Médicos")
    plt.plot(res["timeline_ocupacao"], res["ocupacao"])
    plt.xlabel("Tempo (min)")
    plt.ylabel("Taxa de ocupação")
    plt.grid(True)

    plt.show()

# =========================
# Estudo Paramétrico
# =========================
def estudo_taxa_chegada():
    taxas = range(5, 31, 5)
    medias = []

    for t in taxas:
        r = simula(3, t/60, 15, "exponential", 8*60, lambda x: None)
        esperas = [e for e, _ in r["tempos_espera"]]
        medias.append(np.mean(esperas) if esperas else 0)

    plt.figure("Impacto da Taxa de Chegada")
    plt.plot(taxas, medias, marker="o")
    plt.xlabel("Doentes/hora")
    plt.ylabel("Tempo médio de espera (min)")
    plt.grid(True)
    plt.show()

# =========================
# GUI
# =========================
sg.theme("lightblue")

layout = [
    [sg.Text("Simulação de Clínica Médica", font=("Arial", 16))],
    [sg.Text("Nº Médicos"), sg.Input("3", key="MEDICOS", size=5),
     sg.Text("Taxa chegada (doentes/hora)"), sg.Input("10", key="TAXA", size=5)],
    [sg.Text("Tempo médio consulta (min)"), sg.Input("15", key="TEMPO", size=5),
     sg.Text("Distribuição"),
     sg.Combo(["exponential", "normal", "uniform"], default_value="exponential", key="DIST")],
    [sg.Button("Executar Simulação"), sg.Button("Estudo Taxa Chegada"), sg.Button("Sair")],
    [sg.Multiline(size=(90, 15), key="LOG", disabled=True)]
]

window = sg.Window("Clínica Médica", layout, finalize=True)

# =========================
# Loop principal
# =========================
while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Sair"):
        break

    if event == "Executar Simulação":
        window["LOG"].update("")

        def log(msg):
            window["LOG"].print(msg)

        resultados = simula(
            int(values["MEDICOS"]),
            float(values["TAXA"]) / 60,
            float(values["TEMPO"]),
            values["DIST"],
            8 * 60,
            log
        )

        gerar_graficos(resultados)

    if event == "Estudo Taxa Chegada":
        estudo_taxa_chegada()

window.close()