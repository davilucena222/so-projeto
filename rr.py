# print("")
# print("ROUND ROBIN - QUANTUM 2")
# # construtor da classe "Process", que recebe um identificador (pid), tempo de chegada (arrival_time) e tempo de burst (burst_time)
# def __init__(pid, arrival_time, burst_time):
#     pid = pid # atribui o identificador do processo
#     arrival_time = arrival_time # atribui o tempo de chegada do processo
#     burst_time = burst_time # atribui o tempo de burst do processo
#     remaining_time = burst_time # inicializa o tempo restante do processo com o tempo de burst
#     start_time = None # inicializa o tempo de início do processo como nulo
#     finish_time = None # inicializa o tempo de término do processo como nulo
#     response_time = None # inicializa o tempo de resposta do processo como nulo

# # simula a execução do processo por um período de tempo "quantum"
# def execute(self, current_time):
#     self.start_time = current_time # atribui o tempo de início do processo como o tempo atual
#     if self.response_time is None: # verifica se o tempo de resposta do processo é nulo
#         # calcula o tempo de resposta do processo como a diferença entre o tempo de início e o tempo de chegada
#         self.response_time = self.start_time - self.arrival_time

#     if self.remaining_time <= 2: # verifica se o tempo restante do processo é menor ou igual a 2 
#         # atribui o tempo de término do processo como o tempo atual mais o tempo restante
#         self.finish_time = current_time + self.remaining_time
#         self.remaining_time = 0 # zera o tempo restante do processo
#     else: 
#         # se não, atribui o tempo de término do processo como o tempo atual mais 2 (o valor do quantum)
#         self.finish_time = current_time + 2
#         self.remaining_time -= 2 # decrementa o tempo restante do processo em 2 (o valor do quantum)

#     return self.finish_time # retorna o tempo de término do processo

# def is_completed(self): # verifica se o processo já foi completamente executado
#     return self.remaining_time == 0  # retorna verdadeiro se o tempo restante do processo for igual a zero, falso caso contrário

# def round_robin(processes):
#     n = len(processes) # armazena a quantidade de processos na variável "n"
#     current_time = 0 # define o tempo corrente como 0
#     queue = [] # inicializa a fila de processos como vazia
#     completed_processes = [] # inicializa a lista de processos completados como vazia

#     # enquanto a lista de processos completos for menor que a quantidade de processos
#     while len(completed_processes) < n:
#         for p in processes: 
#             # se o tempo de chegada do processo "p" for menor ou igual ao tempo corrente, e o processo "p" não estiver na fila, e o processo "p" não tiver sido concluído, então adiciona o processo "p" na fila
#             if p.arrival_time <= current_time and p not in queue and not p.is_completed():
#                 queue.append(p)
                
#         if not queue: # se a fila de processos estiver vazia
#             current_time += 1 # incrementa o tempo corrente em 1 e continua o loop
#             continue
#         p = queue.pop(0) # remove o primeiro processo da fila e armazena na variável "p"
#         finish_time = p.execute(current_time) # executa o processo "p" a partir do tempo corrente 
#         if p.is_completed():
#             p.finish_time = finish_time # armazena o tempo de conclusão do processo "p"
#             completed_processes.append(p) # adiciona o processo "p" à lista de processos completos
#         else:
#             queue.append(p) # adiciona o processo "p" de volta à fila

#         # atualiza o tempo corrente com o tempo de conclusão do processo "p"
#         current_time = finish_time 

#     # retorna a lista de processos completos
#     return completed_processes


# if __name__ == '__main__':
#     with open('processos.txt', 'r') as f: # abre o arquivo "processos.txt" para leitura
#         lines = f.readlines() # armazena as linhas do arquivo na variável "lines"
#         processes = []

#         for i, line in enumerate(lines): # percorre cada linha do arquivo
#             arrival_time, burst_time = map(int, line.strip().split()) # armazena o tempo de chegada e o tempo de burst do processo na variável "arrival_time" e "burst_time"
#             processes.append(__init__(i+1, arrival_time, burst_time)) # adiciona o processo na lista de processos e os seus respectivos tempos de chegada e de execução
#     completed_processes = round_robin(processes)  # chamando a função round robin passando a lista de processos 

#     # calcula o tempo de retorno de cada processo
#     tat = [p.finish_time - p.arrival_time for p in completed_processes] 

#     # calcula o tempo de espera de cada processo
#     wt = [p.finish_time - p.arrival_time - p.burst_time for p in completed_processes] 

#     # calcula o tempo de resposta de cada processo
#     rt = [p.response_time for p in completed_processes] 

#     # armazena a quantidade de processos na variável "n"
#     n = len(completed_processes) 

#     avg_tat = sum(tat) / n # calcula o tempo de retorno médio
#     avg_wt = sum(wt) / n # calcula o tempo de espera médio
#     avg_rt = sum(rt) / n # calcula o tempo de resposta médio

#     print(f'Tempo de retorno médio: {avg_tat:.1f}')
#     print(f'Tempo de resposta médio: {avg_rt:.1f}')
#     print(f'Tempo de espera médio: {avg_wt:.1f}')

print("")
print("ROUND ROBIN - QUANTUM 2")

def execute_process(p, current_time):
    start_time = current_time

    if p['response_time'] is None:
        p['response_time'] = start_time - p['arrival_time']

    if p['remaining_time'] <= 2:
        finish_time = current_time + p['remaining_time']
        p['remaining_time'] = 0
    else: 
        finish_time = current_time + 2
        p['remaining_time'] -= 2

    return finish_time


def is_completed(p):
    return p['remaining_time'] == 0


def round_robin(processes):
    n = len(processes)
    current_time = 0
    queue = []
    completed_processes = []

    while len(completed_processes) < n:
        for p in processes:
            if p['arrival_time'] <= current_time and p not in queue and not is_completed(p):
                queue.append(p)

        if not queue:
            current_time += 1
            continue
        
        p = queue.pop(0)
        finish_time = execute_process(p, current_time)

        if is_completed(p):
            p['finish_time'] = finish_time
            completed_processes.append(p)
        else:
            queue.append(p)

        current_time = finish_time 

    return completed_processes


if __name__ == '__main__':
    with open('processos.txt', 'r') as f:
        lines = f.readlines()
        processes = []

        for i, line in enumerate(lines):
            arrival_time, burst_time = map(int, line.strip().split())
            processes.append({'pid': i+1, 'arrival_time': arrival_time, 'burst_time': burst_time, 'remaining_time': burst_time, 'start_time': None, 'finish_time': None, 'response_time': None})

    completed_processes = round_robin(processes)
    print(completed_processes)

    tat = [p['finish_time'] - p['arrival_time'] for p in completed_processes]
    wt = [p['finish_time'] - p['arrival_time'] - p['burst_time'] for p in completed_processes]
    rt = [p['response_time'] for p in completed_processes]

    print(f"PID\tAT\tBT\tFT\tTAT\tWT\tRT")
    for p in completed_processes:
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['finish_time']}\t{tat[p['pid']-1]}\t{wt[p['pid']-1]}\t{rt[p['pid']-1]}")

    print(f"Tempo médio de retorno: {sum(tat)/len(tat)}")
    print(f"Tempo médio de espera: {sum(wt)/len(wt)}")
    print(f"Tempo médio de resposta: {sum(rt)/len(rt)}")
