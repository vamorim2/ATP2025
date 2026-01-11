Simulação de uma Clínica Médica

1. Introdução
Este projeto consiste na implementação de uma simulação de eventos que modela o funcionamento de uma clínica médica. O objetivo principal é estudar o comportamento do sistema (tempos de espera, filas e ocupação dos médicos) sob diferentes parâmetros, recorrendo a processos específicos.

O trabalho foi desenvolvido no âmbito da unidade curricular Algoritmos e Técnicas de Programação na Licenciatura em Engenharia Biomédica (2º ano) da Universidade do Minho.


2. Setup e Execução

2.1 Requisitos
Para executar a simulação são necessárias as seguintes bibliotecas Python:

- numpy
- matplotlib
- simpleGUI

Versão utilizada:
- Python 3.14

2.2 Execução

A simulação pode ser executada de duas formas:

- Via script Python
- Via Jupyter Notebook, esta foi a forma maioritariamente utilizada



3. Descrição do Sistema

O sistema modela uma clínica médica com:

- Doentes que chegam aleatoriamente;
- Médicos que atendem um doente de cada vez;
- Uma fila de espera quando todos os médicos estão ocupados;
- Dois tipos principais de eventos:
  - Chegada de doente
  - Saída de doente (fim da consulta)



4. Parâmetros da Simulação

_Parâmetro_           | _Descrição_                               | _Exemplo_ 
lambda_rate           | Taxa de chegada de doentes (doentes/hora) | 10
num_doctors           | Número de médicos disponíveis             | 3 
service_distribution  | Distribuição do tempo de consulta         | exponential
mean_service_time     | Tempo médio de consulta (minutos)         | 15 
simulation_time       | Duração da simulação (minutos)            | 480 

Distribuições Utilizadas

- Chegadas: Processo de Poisson (λ)
- Tempo de consulta:
  - Exponencial (principal)
  - Normal ou Uniforme (testes alternativos)


5. Métricas e Resultados

Durante a simulação são recolhidas as seguintes métricas:

- Tempo médio de espera
- Tempo médio de consulta
- Tempo médio total na clínica
- Tamanho médio e máximo da fila de espera
- Percentagem de ocupação dos médicos
- Número total de doentes atendidos

Análise dos Resultados

Com parâmetros base (λ=10, 3 médicos, 15 min de consulta):

- Tempos de espera reduzidos;
- Filas pequenas e estáveis;
- Ocupação dos médicos entre 60% e 75%.

Com o aumento da taxa de chegada:

- Crescimento significativo das filas;
- Aumento não linear do tempo de espera;
- Ocupação dos médicos próxima de 100%.


6. Gráficos Produzidos

- Evolução do tamanho da fila ao longo do tempo;
- Evolução da ocupação dos médicos;
- Relação entre taxa de chegada e tamanho médio da fila;
- Comparação entre distribuições do tempo de consulta.


7. Extensões 

- Métricas individuais por médico;
- Uso de dicionário de pessoas para defenir os pacientes;
- Testes com diferentes distribuições estatísticas.



8. Conclusão

A simulação permitiu analisar o impacto de diferentes parâmetros no desempenho de uma clínica médica. O projeto reforça a utilidade de simulações de eventos discretos no apoio à tomada de decisão e dimensionamento de recursos.


Unidade Curricular: Algoritmos e Técnicas de Programação  
Curso: Licenciatura em Engenharia Biomédica (2º ano)  
Instituição: Universidade do Minho – Escola de Engenharia  

Docentes:
- José Carlos Ramalho
- Luís Filipe Cunha

Realizado por:
- Alexandre Ramos
- Vasco Amorim
