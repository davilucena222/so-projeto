                ################################# ALGORITMO FCFS ########################################

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
    print("FIRST COME FIRST SERVE ALGORITHM")
    print(f'Average Turnaround Time: {average_turnaround_time}')
    print(f'Average Waiting Time: {average_waiting_time}')
    print(f'Average Response Time: {average_response_time}')

# abrindo arquivo de leitura
with open("processos.txt", "r") as f:
    lines = f.readlines()
no_of_processes = len(lines)

processData(lines)

            ################################# ALGORITMO SJF ########################################

# abrindo arquivo para leitura
with open('processos.txt', 'r') as f:
    lines = f.readlines()

lengthLine = len(lines) # Obtém o tamanho da lista 


# cria 3 listas todas com o tamanho da lista de processos e inicializa com 0
burst_times = [0] * (lengthLine + 1)
arrival_times = [0] * (lengthLine + 1)
process_info = [0] * (lengthLine + 1)

for i, line in zip(range(lengthLine), lines): # percorre as linhas do arquivo e preenche as listas de tempo de chegada, tempo de burst e informações do processo
    
    arrivalTime, burstTime = line.split() # separa a linha atual em tempo de chegada e tempo de burst
    burst_times[i] = int(burstTime) # converte o tempo de burst em um inteiro e armazena na lista burst_times
    arrival_times[i] = int(arrivalTime) # converte o tempo de chegada em um inteiro e armazena na lista arrival_times
    process_info[i] = [burst_times[i], arrival_times[i], i] # cria uma lista com informações do processo, contendo tempo de burst, tempo de chegada e índice do processo, e armazena na lista process_info

process_info.pop(-1) # remove o último elemento da lista process_info, que foi inicializado com valor zero
sumbt = 0 # variável sumbt com valor zero, será usada para armazenar a soma dos tempos de execução
i = 0 # variável i com valor zero, será o índice do processo atual
ll = [] # cria uma lista vazia chamada que será usada para armazenar os processos que já foram executados

# copia a lista arrival_times para a lista start_times
start_times = arrival_times.copy()

for i in range(0, sum(burst_times)): # loop para simular o escalonamento dos processos
    l = [] # cria uma lista vazia para armazenar os processos que chegaram até o tempo atual 

    # loop para adicionar na lista l os processos que já chegaram
    for j in process_info:
        if j[1] <= i: 
            l.append(j)

    l.sort(key=lambda x: x[0]) # ordena a lista l pelo tempo de burst, do menor para o maior
    process_info[process_info.index(l[0])][0] -= 1  # decrementa em 1 unidade o tempo de execução do primeiro processo na lista l

    for j in process_info: # atualiza a lista start_times para o processo que teve o tempo de execução decrementado, caso seja seu primeiro decremento
        if j[0] == burst_times[j[2]]:
            start_times[j[2]] = i + 1

    for k in process_info: # remove da lista process_info os processos que terminaram de executar e adiciona na lista ll
        if k[0] == 0:
            t = process_info.pop(process_info.index(k))
            ll.append([k, i + 1])


# cria uma lista com tamanho igual ao número de processos + 1, para armazenar os valores de cada processo
ct = [0] * (lengthLine + 1)  # Tempo de conclusão de cada processo
tat = [0] * (lengthLine + 1)  # Tempo de retorno de cada processo
wt = [0] * (lengthLine + 1)  # Tempo de espera de cada processo
rt = [0] * (lengthLine + 1)  # Tempo de resposta de cada processo

# atualiza a lista ct com o tempo de conclusão de cada processo
for i in ll:
    ct[i[0][2]] = i[1]

# calcula as métricas de desempenho para cada processo
for i in range(len(ct)):
    tat[i] = ct[i] - arrival_times[i]  # tempo de retorno é o tempo de conclusão menos o tempo de chegada
    wt[i] = tat[i] - burst_times[i]   # tempo de espera é o tempo de retorno menos o tempo de execução
    rt[i] = start_times[i] - arrival_times[i]  # tempo de resposta é o tempo em que o processo começa a ser executado menos o tempo de chegada

# remove o último elemento de cada lista, que não corresponde a um processo
ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
rt.pop(-1)
burst_times.pop(-1)
arrival_times.pop(-1)

print("")
print("SJF - SHORTEST JOB FIRST - PREEMPTIVE:")
print('Average Waiting Time = ', sum(wt)/len(wt))
print('Average Turnaround Time = ', sum(tat)/len(tat))
print('Average Response Time = ', sum(rt)/len(rt))

        ################################# ALGORITMO ROUND ROBIN ########################################   
        
print("")
print("ROUND ROBIN - QUANTUM 2")
class Process:
    # Construtor da classe "Process", que recebe um identificador (pid), tempo de chegada (arrival_time) e tempo de burst (burst_time)
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid # atribui o identificador do processo
        self.arrival_time = arrival_time # atribui o tempo de chegada do processo
        self.burst_time = burst_time # atribui o tempo de burst do processo
        self.remaining_time = burst_time # inicializa o tempo restante do processo com o tempo de burst
        self.start_time = None # inicializa o tempo de início do processo como nulo
        self.finish_time = None # inicializa o tempo de término do processo como nulo
        self.response_time = None # inicializa o tempo de resposta do processo como nulo

    # Simula a execução do processo por um período de tempo "quantum"
    def execute(self, current_time):
        self.start_time = current_time # atribui o tempo de início do processo como o tempo atual

        # Verifica se o tempo de resposta do processo é nulo
        if self.response_time is None:
            self.response_time = self.start_time - self.arrival_time # se sim, calcula o tempo de resposta do processo como a diferença entre o tempo de início e o tempo de chegada
    
        if self.remaining_time <= 2: # verifica se o tempo restante do processo é menor ou igual a 2 
            self.finish_time = current_time + self.remaining_time # se sim, atribui o tempo de término do processo como o tempo atual mais o tempo restante
            self.remaining_time = 0 # zera o tempo restante do processo
        else: # se não, atribui o tempo de término do processo como o tempo atual mais 2 (o valor do quantum)
            self.finish_time = current_time + 2
            self.remaining_time -= 2 # decrementa o tempo restante do processo em 2 (o valor do quantum)
        
        return self.finish_time # retorna o tempo de término do processo

def is_completed(self): # verifica se o processo já foi completamente executado
    return self.remaining_time == 0 # retorna verdadeiro se o tempo restante do processo for igual a zero, falso caso contrário

def round_robin(processes):
    n = len(processes) # armazena a quantidade de processos na variável "n"
    current_time = 0 # define o tempo corrente como 0
    queue = [] # inicializa a fila de processos como vazia
    completed_processes = [] # inicializa a lista de processos completados como vazia

    while len(completed_processes) < n: # enquanto a lista de processos completos for menor que a quantidade de processos

        # itera sobre a lista de processos
        for p in processes: 
            # se o tempo de chegada do processo "p" for menor ou igual ao tempo corrente, e o processo "p" não estiver na fila, e o processo "p" não tiver sido concluído, então adiciona o processo "p" na fila
            if p.arrival_time <= current_time and p not in queue and not p.is_completed(): 
                queue.append(p)

        if not queue: # se a fila de processos estiver vazia
            current_time += 1 # incrementa o tempo corrente em 1 e continua o loop
            continue 

        p = queue.pop(0) # remove o primeiro processo da fila e armazena na variável "p"
        finish_time = p.execute(current_time) # executa o processo "p" a partir do tempo corrente e armazena o tempo de conclusão
        
        if p.is_completed(): # se o processo "p" tiver sido concluído
            p.finish_time = finish_time # armazena o tempo de conclusão do processo "p"
            completed_processes.append(p) # adiciona o processo "p" à lista de processos completos
        else: # se o processo "p" não tiver sido concluído
            queue.append(p) # adiciona o processo "p" de volta à fila
        current_time = finish_time # atualiza o tempo corrente com o tempo de conclusão do processo "p"
    return completed_processes # retorna a lista de processos completos


if __name__ == '__main__':
    with open('processos.txt', 'r') as f:  
        lines = f.readlines()
        processes = []
        for i, line in enumerate(lines):
            arrival_time, burst_time = map(int, line.strip().split())
            processes.append(Process(i+1, arrival_time, burst_time))
    completed_processes = round_robin(processes)
    tat = [p.finish_time - p.arrival_time for p in completed_processes]
    wt = [p.finish_time - p.arrival_time - p.burst_time for p in completed_processes]
    rt = [p.response_time for p in completed_processes]
    n = len(completed_processes)
    avg_tat = sum(tat) / n
    avg_wt = sum(wt) / n
    avg_rt = sum(rt) / n
    print(f'Tempo de retorno médio: {avg_tat:.1f}')
    print(f'Tempo de resposta médio: {avg_rt:.1f}')
    print(f'Tempo de espera médio: {avg_wt:.1f}')