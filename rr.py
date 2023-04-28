print("")
print("ROUND ROBIN - QUANTUM 2")

def execute_process(p, current_time): 
    start_time = current_time 

    if p['start_time'] is None:
        p['start_time'] = start_time

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
    procExec = []

    while len(completed_processes) < n:
        print("")
        print("tamanho da fila: ", len(queue)) # []
        print("fila: ", queue)
        print("")

        if len(queue) > 0:
            procExec.append(queue.pop(0))

        j = 0

        if len(processes) > 0: # [p1(0, 20), p2(0, 10), p3(4, 6), p4(4, 8)]
            for p in processes:
                if len(queue) > 0 and current_time > 0:
                    if p['arrival_time'] <= current_time and p not in queue and not is_completed(p):
                        queue.insert(j, p)
                        # processes.remove(p)
                elif p and p['arrival_time'] <= current_time and p not in queue and not is_completed(p):
                    queue.append(p) # [p1(0, 20)]
                    # processes.remove(p)

                j = j + 1

        if len(queue) > 0:
            for p in queue:
                if 

        # if not queue:
            # current_time += 1
            # continue

        p = procExec.pop(0) if len(procExec) > 0 else queue.pop(0) # p = , queue = [p2(10), p1(18)], proExec = []
        finish_time = execute_process(p, current_time) 

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