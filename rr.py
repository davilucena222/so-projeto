print("")
print("ROUND ROBIN - QUANTUM 2")

def execute_process(p, current_time): # ['pid': B, 'arrival_time': 0, 'burst_time': 10, 'remaining_time': 8, 'start_time': 2, 'finish_time': None, 'response_time': 2],
    start_time = current_time # start_time = 2

    if p['start_time'] is None:
        p['start_time'] = start_time

    if p['response_time'] is None:
        p['response_time'] = start_time - p['arrival_time']

    if p['remaining_time'] <= 2:
        finish_time = current_time + p['remaining_time']
        p['remaining_time'] = 0
    else: 
        finish_time = current_time + 2  # finish_time = 4
        p['remaining_time'] -= 2

    return finish_time

def is_completed(p):
    return p['remaining_time'] == 0


def round_robin(processes):
    n = len(processes) 
    current_time = 0  
    queue = []
    completed_processes = []
    partial = []

    # ordenando processos pelo tempo de chegada
    # processes = sorted(processes, key=lambda p: p['arrival_time'])
    # print("ordenado: ", processes)

    while len(completed_processes) < n:

        if len(processes) != 0: 
            for p in processes:
                if p['arrival_time'] <= current_time and p not in queue and not is_completed(p):
                    queue.append(p)
                    processes.remove(p)

        if not queue:
            current_time += 1
            continue
        
        p = queue.pop(0)  
        finish_time = execute_process(p, current_time) 

        if len(processes) != 0:
            for processo in processes:
                if processo['arrival_time'] <= finish_time and processo not in queue and not is_completed(p):
                    partial.append(processo)
                    processes.remove(processo)

        print("partial: ", partial)
        
        j = 0

        if len(partial) != 0:
            while len(partial) != 0:
                proc = partial.pop(0)
                if proc:
                    queue.insert(j, proc)
                    j += 1

        if is_completed(p): 
            p['finish_time'] = finish_time
            completed_processes.append(p)
        else:
            queue.append(p)

        current_time = finish_time

    return completed_processes

# execução do main
if __name__ == '__main__':
    with open('processos.txt', 'r') as f:
        lines = f.readlines()
        processes = []

        for i, line in enumerate(lines):
            arrival_time, burst_time = map(int, line.strip().split())
            processes.append({'pid': i+1, 'arrival_time': arrival_time, 'burst_time': burst_time, 'remaining_time': burst_time, 'start_time': None, 'finish_time': None, 'response_time': None})

    completed_processes = round_robin(processes)

    tat = [p['finish_time'] - p['arrival_time'] for p in completed_processes]
    wt = [p['finish_time'] - p['arrival_time'] - p['burst_time'] for p in completed_processes]
    rt = [p['response_time'] for p in completed_processes]

    print(f"PID\tAT\tBT\tFT\tTAT\tWT\tRT")
    for p in completed_processes:
        print(f"{p['pid']}\t{p['arrival_time']}\t{p['burst_time']}\t{p['finish_time']}\t{tat[p['pid']-1]}\t{wt[p['pid']-1]}\t{rt[p['pid']-1]}")

    print(f"Tempo médio de retorno: {sum(tat)/len(tat)}")
    print(f"Tempo médio de espera: {sum(wt)/len(wt)}")
    print(f"Tempo médio de resposta: {sum(rt)/len(rt)}")