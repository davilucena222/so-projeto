# abrindo arquivo para letura
with open('processos.txt', 'r') as f:
    lines = f.readlines()

# contabilizando a quantidade de linhas presentes no arquivo
lengthLine = len(lines)

# inicializando os arrays que vão armazenar os tempos de chegada, execução e informações do processo
burst_times = [0] * (lengthLine + 1)
arrival_times = [0] * (lengthLine + 1)
process_info = [0] * (lengthLine + 1)

# percorre o array de linhas do arquivo e armazena os tempos de chegada e execução em seus respectivos arrays
for i, line in zip(range(lengthLine), lines):
    arrivalTime, burstTime = line.split()
    burst_times[i] = int(burstTime)
    arrival_times[i] = int(arrivalTime)
    process_info[i] = [burst_times[i], arrival_times[i], i]

# retirando o último zero do array de informações do processo
process_info.pop(-1)
sumbt = 0 
i = 0
ll = []

# inicializando o array de tempos de início com os tempos de chegada
start_times = arrival_times.copy()

# enquanto o array de processos não estiver vazio, o algoritmo continua
for i in range(0, sum(burst_times)):
    # l = [j for j in process_info if j[1] <= i]
    l = []

    # pega o processo com o menor tempo de execução que chegou
    for j in process_info:
        if j[1] <= i:
            l.append(j)

    # ordena os processos com menor tempo de execução que chegou
    l.sort(key=lambda x: x[0])

    # atualiza o tempo de execução do processo e diminui ele em 1 unidade de tempo
    process_info[process_info.index(l[0])][0] -= 1
    # print(l)

    # Atualiza o tempo de início do processo se for a primeira vez que ele está recebendo a CPU
    for j in process_info:
        if j[0] == burst_times[j[2]]:
            start_times[j[2]] = i + 1

    # se o processo tiver tempo de execução igual a zero, ele é removido do array de processos e adicionado ao array de tempos de conclusão
    for k in process_info:
        if k[0] == 0:
            t = process_info.pop(process_info.index(k))
            ll.append([k, i + 1])

# inicializando os arrays de tempos de conclusão, tempo de resposta, tempo de espera e tempo de retorno
ct = [0] * (lengthLine + 1)
tat = [0] * (lengthLine + 1)
wt = [0] * (lengthLine + 1)
rt = [0] * (lengthLine + 1)

# adiciona os tempos de conclusão no array de tempos de conclusão
for i in ll:
    ct[i[0][2]] = i[1] 

# calcula os tempos de resposta, espera e retorno
for i in range(len(ct)):
    tat[i] = ct[i] - arrival_times[i]
    wt[i] = tat[i] - burst_times[i]
    rt[i] = start_times[i] - arrival_times[i]

# retirando o último zero do array de tempos de conclusão
ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
rt.pop(-1)
burst_times.pop(-1)
arrival_times.pop(-1)

print("SJF - SHORTEST JOB FIRST:")
print('Average Waiting Time = ', sum(wt)/len(wt))
print('Average Turnaround Time = ', sum(tat)/len(tat))
print('Average Response Time = ', sum(rt)/len(rt))