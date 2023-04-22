if __name__ == '__main__':
    # Python program for implementation of RR Scheduling
    print("Enter Total Process Number: ")
    total_p_no = int(input()) # 5
    total_time = 0  
    total_time_counted = 0
    array_waiting_time = []
    array_turnaround_time = []

    # proc is process list
    proc = []
    wait_time = 0
    turnaround_time = 0

    for _ in range(total_p_no):
        # Getting the input for process
        print("Enter process arrival time and burst time") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        # processes are appended to the proc list in following format
        proc.append([arrival, burst, remaining_time, 0])
        # total_time gets incremented with burst time of each process
        total_time += burst

    print("Enter time quantum")
    time_quantum = int(input())

    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            if proc[i][2] >= time_quantum:
                total_time_counted = total_time_counted + time_quantum
            elif proc[i][2] == 1:
                total_time_counted = total_time_counted + proc[i][2]
            else:
                continue

            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                # total_time_counted = total_time_counted + proc[i][2]
                total_time = total_time - proc[i][2]
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] = proc[i][2] - time_quantum
                total_time = total_time - time_quantum
                # total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                # if remaining time of process is 0
                # and 
                # individual waiting time of process has not been calculated i.e flag
                if len(array_waiting_time) == 0 or len(array_turnaround_time) != 0:
                    wait_time = wait_time - total_time_counted - proc[i][0] - proc[i][1]

                    if abs(wait_time) >= total_time_counted:
                        wait_time = 0
                        wait_time = total_time_counted - proc[i][0] - proc[i][1]
                        array_waiting_time = [wait_time]
                    else:
                        array_waiting_time = [wait_time]
               
                if proc[i + 1][2] and proc[i + 1][2] > 2:
                    turnaround_time = (total_time_counted + 2) - turnaround_time 
                    array_turnaround_time = [turnaround_time]
                else:
                    turnaround_time = turnaround_time + total_time_counted - proc[i][0]
                    
                    if turnaround_time >= total_time_counted:
                        turnaround_time = (total_time_counted) - proc[i][0]
                        array_waiting_time = [turnaround_time]     
                        
                    array_waiting_time = [turnaround_time]

                # flag is set to 1 once wait time is calculated
                proc[i][3] = 1 

    print("\nAvg Waiting Time is ", (wait_time * 1) / total_p_no)
    print("Avg Turnaround Time is ", (turnaround_time * 1) / total_p_no)