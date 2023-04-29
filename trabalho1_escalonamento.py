            ################################# ALGORITMO FCFS (COMPLETO) ########################################
# abrindo arquivo de leitura
with open("processos.txt", "r") as f:
    lines = f.readlines()
no_of_processes = len(lines)

# esta função recebe uma lista de processos
def processData(lines):
    process_data = [] # cria uma lista vazia para armazenar os processos

    for i, line in enumerate(lines): # percorre a lista e obtém os dados de tempo de chegada e tempo de execução 
        temporary = [] # cria uma lista temporária vazia para armazenar os dados de cada processo
        arrival_time, burst_time = line.split() # extrai o tempo de chegada e o tempo de execução
        temporary.extend([i+1, int(arrival_time), int(burst_time)]) # adiciona o índice atual, o tempo de chegada e o tempo de execução de cada processo à lista temporária 
        process_data.append(temporary) # adiciona a lista temporária à lista de dados de processos usando o método append()

    # chama a função schedulingProcess() passando a lista de dados de processos como argumento
    schedulingProcess(process_data)


# função que recebe uma lista de dados de processos para realizar o escalonamento e os cálculos
def schedulingProcess(process_data):
    process_data.sort(key=lambda x: x[1]) # ordena os dados do processo pela ordem de chegada (arrival time)

    # duas listas vazias para armazenar os tempos de início e fim de cada processo
    start_time = []
    exit_time = []

    # inicializa o tempo atual (s_time)
    s_time = 0

    # percorre todos os processos na lista de dados 
    for i in range(len(process_data)):
        if s_time < process_data[i][1]: # verifica se o tempo atual é menor que o tempo de chegada do processo atual
            s_time = process_data[i][1] # define o tempo de início do processo atual como o tempo de chegada do processo para sua execução

        start_time.append(s_time) # adiciona o tempo de início do processo atual à lista de tempos de início
        s_time = s_time + process_data[i][2] # adiciona o tempo de execução do processo atual ao tempo atual (s_time)
        e_time = s_time # define o tempo de término do processo atual como o tempo atual (s_time)
        exit_time.append(e_time) # adiciona o tempo de término do processo atual à lista de tempos de término
        process_data[i].append(e_time) # Adiciona o tempo de término do processo atual aos dados de processo

    # calcula os tempos de resposta (turnaround time), de espera (waiting time) e de resposta (response time) usando funções auxiliares
    t_time = calculateTurnaroundTime(process_data)
    w_time = calculateWaitingTime(process_data)
    r_time = calculateResponseTime(process_data, start_time)

    # função que imprime os tempos de resposta, de espera e de resposta para os processos
    printData(t_time, w_time, r_time)

# calcula o tempo de retorno 
def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0  # inicializa a variável "total_turnaround_time" com o valor zero
    for i in range(len(process_data)):  # loop for que percorre a lista de processos
        turnaround_time = process_data[i][3] - process_data[i][1]  # calcula o tempo de resposta do processo atual
        total_turnaround_time = total_turnaround_time + turnaround_time  # adiciona o tempo de resposta do processo atual ao total de tempo de resposta
        process_data[i].append(turnaround_time)  # adiciona o tempo de resposta do processo atual à lista de dados do processo
    average_turnaround_time = total_turnaround_time / len(process_data)  # calcula o tempo de resposta médio 

    return average_turnaround_time # retorna o tempo de resposta médio

# função para calcular o tempo de espera
def calculateWaitingTime(process_data):
    total_waiting_time = 0  # inicializa a variável "total_waiting_time" com o valor zero
    for i in range(len(process_data)):  # loop que percorre a lista de processos 
        waiting_time = process_data[i][4] - process_data[i][2]  # calcula o tempo de espera do processo atual
        total_waiting_time = total_waiting_time + waiting_time  # adiciona o tempo de espera do processo atual ao total de tempo de espera
        process_data[i].append(waiting_time)  # adiciona o tempo de espera do processo atual à lista de dados do processo
    average_waiting_time = total_waiting_time / len(process_data)  # calcula o tempo de espera médio 
    return average_waiting_time  # retorna o tempo de espera médio


def calculateResponseTime(process_data, start_time):
    total_response_time = 0  # Inicializa a variável "total_response_time" com o valor zero
    for i in range(len(process_data)):  # Loop que percorre a lista de processos "process_data"
        response_time = start_time[i] - process_data[i][1]  # Calcula o tempo de resposta do processo atual
        total_response_time = total_response_time + response_time  # Adiciona o tempo de resposta do processo atual ao total de tempo de resposta
        process_data[i].append(response_time)  # Adiciona o tempo de resposta do processo atual à lista de dados do processo
    average_response_time = total_response_time / len(process_data)  # calcula o tempo de resposta médio 
    return average_response_time  # retorna o tempo de resposta médio

# função para imprimir os tempos 
def printData(average_turnaround_time, average_waiting_time, average_response_time):
    print("")
    print("FIRST COME FIRST SERVE ALGORITHM")
    print("")
    print(f'Tempo de retorno médio: {average_turnaround_time:.1f}')
    print(f'Tempo de resposta médio: {average_response_time:.1f}')
    print(f'Tempo de espera médio: {average_waiting_time:.1f}')


# chamada da função processData para inicializar o algoritmo
processData(lines)

            ################################# ALGORITMO SJF NÃO PREEMPETIVO ########################################

print("")
print("SFJ - SHORTEST JOB FIRST - Non-Preemptive")
print("")
# with open('processos.txt') as f:
#     lines = f.readlines()

bt = []
for i, line in enumerate(lines):
    at, bt_i = map(int, line.strip().split())
    bt.append((at, bt_i, i))

bt.sort()

n = len(bt)
ct = [0] * no_of_processes
tat = [0] * no_of_processes
wt = [0] * no_of_processes
rt = [0] * no_of_processes

t = 0
while bt:
    available_processes = [p for p in bt if p[0] <= t]
    if not available_processes:
        t += 1
        continue
    next_process = min(available_processes, key=lambda p: p[1])
    bt.remove(next_process)
    at, bt_i, i = next_process
    ct[i] = t + bt_i
    tat[i] = ct[i] - at
    wt[i] = tat[i] - bt_i
    rt[i] = t - at
    t = ct[i]

for i, p in enumerate(bt):
    at, bt_i, _ = p
    print(f'P{i}\t{at}\t{bt_i}\t{ct[i]}\t{tat[i]}\t{wt[i]}\t{rt[i]}')
    
print(f'Tempo de Retorno Médio: {sum(tat)/no_of_processes:.1f}')
print(f'Tempo de Resposta Médio: {sum(rt)/no_of_processes:.1f}')
print(f'Tempo de Espera Médio: {sum(wt)/no_of_processes:.1f}')

        ################################# ALGORITMO ROUND ROBIN (AJEITANDO...) ########################################   
        
# with open("processos.txt", "r") as arquivo:
#   linhas = arquivo.readlines()
  
processos = []
j = 0
for linha in lines:
  tempo_de_chegada, tempo_de_execucao = map(int, linha.strip().split())
  
  j += 1

  processos.append({
    "pid": j,
    "tempo_de_chegada": tempo_de_chegada,
    "tempo_de_execucao": tempo_de_execucao,
    "tempo_restante": tempo_de_execucao,
    "tempo_de_inicio": None,
    "tempo_de_finalizacao": None,
    "tempo_de_resposta": None,
    "tempo_de_espera": None
  })

def executa_processo(processo, tempo_atual):
  tempo_corrido = tempo_atual

  if processo["tempo_de_inicio"] == None:
    processo["tempo_de_inicio"] = tempo_atual

  if processo["tempo_restante"] > 2:
    processo["tempo_restante"] = processo["tempo_restante"] - 2
    tempo_corrido = tempo_corrido + 2
    
    if processo["tempo_de_resposta"] == None:
      processo["tempo_de_resposta"] = tempo_corrido

  elif processo["tempo_restante"] == 1:
    processo["tempo_restante"] = processo["tempo_restante"] - 1
    processo["tempo_restante"] = 0
    tempo_corrido = tempo_corrido + 1
    processo["tempo_de_finalizacao"] = tempo_corrido
  elif processo["tempo_restante"] == 2:
    processo["tempo_restante"] = processo["tempo_restante"] - 2
    processo["tempo_restante"] = 0
    tempo_corrido = tempo_corrido + 2
    processo["tempo_de_finalizacao"] = tempo_corrido
  
  return tempo_corrido

processos.sort(key = lambda x: x["tempo_de_chegada"])

fila_de_espera = []
processos_encerrados = []
primeiros_processos = []
tempo_atual = 0
tempo_de_espera = 0
tempo_de_resposta = 0
num_processos = len(processos)
tempo_de_chegada_primeiro_processo = processos[0]["tempo_de_chegada"]

while len(processos_encerrados) < num_processos:
  if len(processos) > 0:
    for processo_executa in processos:
      if processo_executa["tempo_de_chegada"] <= tempo_atual and processo_executa not in fila_de_espera and not processo_executa["tempo_restante"] == 0:
        fila_de_espera.append(processo_executa)

      if tempo_atual == tempo_de_chegada_primeiro_processo and processo_executa["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo:
        primeiros_processos.append(processo_executa)

  if len(fila_de_espera) == 0:
    tempo_atual = tempo_atual + 1
    continue

  processo = fila_de_espera.pop(0)
  tempo_final = executa_processo(processo, tempo_atual)

  if len(processos) > 0:
    for novo_processo in processos:
      if novo_processo["tempo_de_chegada"] <= tempo_final and novo_processo not in fila_de_espera and not novo_processo["tempo_restante"] == 0 and not novo_processo["pid"] == processo["pid"]:
        fila_de_espera.append(novo_processo)

  if len(fila_de_espera) > 0:
    for proc in fila_de_espera:

      if proc["tempo_de_espera"] == None and proc["tempo_de_chegada"] == tempo_de_chegada_primeiro_processo and proc in primeiros_processos and proc["tempo_de_resposta"] != None:
        proc["tempo_de_espera"] = tempo_final - tempo_atual
      elif proc["tempo_de_espera"] == None:
        proc["tempo_de_espera"] = tempo_final - proc["tempo_de_chegada"]
      else:
        proc["tempo_de_espera"] = proc["tempo_de_espera"] + (tempo_final - tempo_atual)

  if processo["tempo_restante"] == 0:
    if processo["tempo_de_espera"] == None:
      processo["tempo_de_espera"] = 0
    processos_encerrados.append(processo)
  else:
    fila_de_espera.append(processo)
    
  tempo_atual = tempo_final

tempo_medio_de_retorno = [pp1["tempo_de_finalizacao"] - pp1["tempo_de_chegada"] for pp1 in processos_encerrados]
tempo_medio_de_resposta = [pp2["tempo_de_inicio"] - pp2["tempo_de_chegada"] for pp2 in processos_encerrados]
tempo_medio_espera = [pp3["tempo_de_espera"] for pp3 in processos_encerrados]

print("")
print("ROUND ROBIN QUANTUM 2")
print("")
print(f"Tempo médio de retorno: {sum(tempo_medio_de_retorno) / len(tempo_medio_de_retorno):.1f}")
print(f"Tempo médio de resposta: {sum(tempo_medio_de_resposta) / len(tempo_medio_de_resposta):.1f}")
print(f"Tempo médio de espera: {sum(tempo_medio_espera) / len(tempo_medio_espera):.1f}")