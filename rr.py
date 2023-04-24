print("")
print("ROUND ROBIN - QUANTUM 2")
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid 
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.finish_time = None
        self.response_time = None
    
    def execute(self, current_time):
        self.start_time = current_time
        if self.response_time is None:
            self.response_time = self.start_time - self.arrival_time
        if self.remaining_time <= 2:
            self.finish_time = current_time + self.remaining_time
            self.remaining_time = 0
        else:
            self.finish_time = current_time + 2
            self.remaining_time -= 2
        return self.finish_time
    
    def is_completed(self):
        return self.remaining_time == 0


def round_robin(processes):
    n = len(processes)
    current_time = 0
    queue = []
    completed_processes = []
    while len(completed_processes) < n:
        for p in processes:
            if p.arrival_time <= current_time and p not in queue and not p.is_completed():
                queue.append(p)
        if not queue:
            current_time += 1
            continue
        p = queue.pop(0)
        finish_time = p.execute(current_time)
        if p.is_completed():
            p.finish_time = finish_time
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