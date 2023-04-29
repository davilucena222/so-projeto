def round_robin(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    processes = []
    for line in lines:
        arrival_time, burst_time = map(int, line.strip().split())
        processes.append({'arrival_time': arrival_time, 'burst_time': burst_time, 'remaining_time': burst_time, 'start_time': None, 'end_time': None, 'response_time': None})

    processes.sort(key=lambda x: x['arrival_time'])  # ordena os processos pelo tempo de chegada

    queue = []
    current_time = 0
    waiting_time = 0
    response_time = 0
    for process in processes:
        while current_time < process['arrival_time'] or (not queue and current_time == process['arrival_time']):
            current_time += 1

        queue.append(process)

        while queue:
            current_process = queue.pop(0)

            if current_process['start_time'] is None:
                current_process['response_time'] = current_time - current_process['arrival_time']
                response_time += current_process['response_time']
                current_process['start_time'] = current_time

            if current_process['remaining_time'] > 2:
                current_process['remaining_time'] -= 2
                current_time += 2
                queue.append(current_process)
            else:
                current_time += current_process['remaining_time']
                current_process['end_time'] = current_time
                waiting_time += current_process['end_time'] - current_process['arrival_time'] - current_process['burst_time']

            # insere novos processos na fila após o próximo processo ser retirado
            if queue and queue[0]['arrival_time'] > current_time:
                break

    num_processes = len(processes)
    print(processes)
    avg_response_time = sum(process['start_time'] - process['response_time'] for process in processes) / num_processes
    avg_waiting_time = waiting_time / num_processes
    avg_turnaround_time = sum(process['end_time'] - process['arrival_time'] for process in processes) / num_processes

    print(f"Tempo médio de resposta: {avg_response_time:.2f}")
    print(f"Tempo médio de espera: {avg_waiting_time:.2f}")
    print(f"Tempo médio de retorno: {avg_turnaround_time:.2f}")

round_robin('processos.txt')

