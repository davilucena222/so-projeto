class FCFS:
    def processData(self, lines):
        process_data = []
        for i, line in enumerate(lines):
            temporary = []
            arrival_time, burst_time = line.split()
            temporary.extend([i+1, int(arrival_time), int(burst_time)])
            process_data.append(temporary)
        FCFS.schedulingProcess(self, process_data)

    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[1])
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            if s_time < process_data[i][1]:
                s_time = process_data[i][1]
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)
        t_time = FCFS.calculateTurnaroundTime(self, process_data)
        w_time = FCFS.calculateWaitingTime(self, process_data)
        r_time = FCFS.calculateResponseTime(self, process_data, start_time)
        FCFS.printData(self, process_data, t_time, w_time, r_time)

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)

        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][4] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)

        return average_waiting_time

    def calculateResponseTime(self, process_data, start_time):
        total_response_time = 0
        for i in range(len(process_data)):
            response_time = start_time[i] - process_data[i][1]
            total_response_time = total_response_time + response_time
            process_data[i].append(response_time)
        average_response_time = total_response_time / len(process_data)

        return average_response_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time, average_response_time):

        print("Process_ID  Arrival_Time  Burst_Time  Completion_Time  Turnaround_Time  Waiting_Time  Response_Time")

        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="				")
            print()

        print(f'Average Turnaround Time: {average_turnaround_time}')

        print(f'Average Waiting Time: {average_waiting_time}')

        print(f'Average Response Time: {average_response_time}')

if __name__ == "__main__":
    with open("processos.txt", "r") as f:
        lines = f.readlines()
    no_of_processes = len(lines)

    fcfs = FCFS()
    fcfs.processData(lines)