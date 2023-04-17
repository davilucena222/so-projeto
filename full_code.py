print("")
print("FCFS - FIRST-COME-FIRST-SERVED")

with open("processos.txt", "r") as file:
    d = dict()
    for i, line in enumerate(file):
        key = "P" + str(i + 1)
        a, b = map(int, line.strip().split())
        l = [a, b]
        d[key] = l

n = len(d)
d = sorted(d.items(), key=lambda item: item[1][0])

ET = []
TR = []
RT = []
for i in range(len(d)):
    # first process
    if i == 0:
        ET.append(d[i][1][1])
        TR.append(d[i][1][1] - d[i][1][0])
        RT.append(TR[i])

    # get prevET + newBT
    else:
        ET.append(ET[i - 1] + d[i][1][1])
        TR.append(ET[i] - d[i][1][0])
        RT.append(TR[i] - d[i - 1][1][1])

TAT = []
WT = []
for i in range(len(d)):
    TAT.append(ET[i] - d[i][1][0])
    WT.append(TAT[i] - d[i][1][1])
    RT[i] = ET[i - 1] - d[i][1][0] if i > 0 else 0

avg_WT = sum(WT) / n
avg_TRT = sum(TAT) / n
avg_TR = sum(RT) / n

print("Tempo de retorno médio: ", avg_TRT)
print("Tempo de resposta médio: ", avg_TR)
print("Tempo de espera médio: ", avg_WT)

print("")
print("SFJ - SHORTEST JOB FIRST")
with open('processos.txt') as f:
    lines = f.readlines()

bt = []
for i, line in enumerate(lines):
    at, bt_i = map(int, line.strip().split())
    bt.append((at, bt_i, i))

bt.sort()

n = len(bt)
ct = [0] * n
tat = [0] * n
wt = [0] * n
rt = [0] * n

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
print(f'Tempo de Retorno Médio: {sum(tat)/n:.1f}')
print(f'Tempo de Resposta Médio: {sum(rt)/n:.1f}')
print(f'Tempo de Espera Médio: {sum(wt)/n:.1f}')

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




# print("ROUND ROBIN - QUANTUM 2")
# class Process:
#     def __init__(self, pid, arrival_time, burst_time):
#         self.pid = pid
#         self.arrival_time = arrival_time
#         self.burst_time = burst_time
#         self.remaining_time = burst_time
#         self.start_time = None
#         self.finish_time = None
#         self.response_time = None
    
#     def execute(self, current_time):
#         self.start_time = current_time
#         if self.response_time is None:
#             self.response_time = self.start_time - self.arrival_time
#         if self.remaining_time <= 2:
#             self.finish_time = current_time + self.remaining_time
#             self.remaining_time = 0
#         else:
#             self.finish_time = current_time + 2
#             self.remaining_time -= 2
#         return self.finish_time
    
#     def is_completed(self):
#         return self.remaining_time == 0


# def round_robin(processes):
#     n = len(processes)
#     current_time = 0
#     queue = []
#     completed_processes = []
#     while len(completed_processes) < n:
#         for p in processes:
#             if p.arrival_time <= current_time and p not in queue and not p.is_completed():
#                 queue.append(p)
#         if not queue:
#             current_time += 1
#             continue
#         p = queue.pop(0)
#         finish_time = p.execute(current_time)
#         if p.is_completed():
#             p.finish_time = finish_time
#             completed_processes.append(p)
#         else:
#             queue.append(p)
#         current_time = finish_time
#     return completed_processes


# if __name__ == '__main__':
#     with open('processos.txt', 'r') as f:
#         lines = f.readlines()
#         processes = []
#         for i, line in enumerate(lines):
#             arrival_time, burst_time = map(int, line.strip().split())
#             processes.append(Process(i+1, arrival_time, burst_time))
#     completed_processes = round_robin(processes)
#     tat = [p.finish_time - p.arrival_time for p in completed_processes]
#     wt = [p.finish_time - p.arrival_time - p.burst_time for p in completed_processes]
#     rt = [p.response_time for p in completed_processes]
#     n = len(completed_processes)
#     avg_tat = sum(tat) / n
#     avg_wt = sum(wt) / n
#     avg_rt = sum(rt) / n
#     print(f'Average TAT: {avg_tat:.2f}')
#     print(f'Average WT: {avg_wt:.2f}')
#     print(f'Average RT: {avg_rt:.2f}')