with open('processos.txt', 'r') as f:
  lines = f.readlines()

lengthLine = len(lines)

burst_times = [0] * (lengthLine + 1)
arrival_times = [0] * (lengthLine + 1)
process_info = [0] * (lengthLine + 1)

for i, line in zip(range(lengthLine), lines):
    arrivalTime, burstTime = line.split()
    burst_times[i] = int(burstTime)
    arrival_times[i] = int(arrivalTime)
    process_info[i] = [burst_times[i], arrival_times[i], i]

process_info.pop(-1)
sumbt = 0 
i = 0
ll = []

for i in range(0, sum(burst_times)):
	l = [j for j in process_info if j[1] <= i]
	l.sort(key=lambda x: x[0])
	process_info[process_info.index(l[0])][0] -= 1
	for k in process_info:
		if k[0] == 0:
			t = process_info.pop(process_info.index(k))
			ll.append([k, i + 1])

ct = [0] * (lengthLine + 1)
tat = [0] * (lengthLine + 1)
wt = [0] * (lengthLine + 1)

for i in ll:
	ct[i[0][2]] = i[1] 

for i in range(len(ct)):
	tat[i] = ct[i] - arrival_times[i]
	wt[i] = tat[i] - burst_times[i]

ct.pop(-1)
wt.pop(-1)
tat.pop(-1)
burst_times.pop(-1)
arrival_times.pop(-1)

print("SJF - SHORTEST JOB FIRST:")
print('Average Waiting Time = ', sum(wt)/len(wt))
print('Average Turnaround Time = ', sum(tat)/len(tat))