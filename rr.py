if __name__ == '__main__':
    # Python program for implementation of RR Scheduling
    print("Enter Total Process Number: ")
    total_p_no = int(input())
    total_time = 0 
    total_time_counted = 0
    # proc is process list
    proc = []
    wait_time = 0
    response_time = 0 # new variable to keep track of response time
    turnaround_time = 0
    for _ in range(total_p_no):
        # Getting the input for process
        print("Enter process arrival time and burst time") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        # processes are appended to the proc list in following format
        proc.append([arrival, burst, remaining_time, 0, 0]) # new element for start time
        # total_time gets incremented with burst time of each process
        total_time += burst
    print("Enter time quantum")
    time_quantum = int(input())
    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0 
                if proc[i][3] == 0:
                    # if process has not started yet, set start time
                    proc[i][4] = total_time_counted - proc[i][1] # start time = current time - burst time
                    proc[i][3] = 1 # flag to indicate start time has been set
            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
                if proc[i][3] == 0:
                    # if process has not started yet, set start time
                    proc[i][4] = total_time_counted - time_quantum # start time = current time - quantum
                    proc[i][3] = 1 # flag to indicate start time has been set
            if proc[i][2] == 0 and proc[i][3] != 2:
                # if remaining time of process is 0
                # and 
                # individual waiting time of process has not been calculated i.e flag
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                response_time += proc[i][4] - proc[i][0] # calculating response time
                turnaround_time += total_time_counted - proc[i][0] # calculating turnaround time
                proc[i][3] = 2 # flag to indicate that waiting time has been calculated

    # Output
    print("\nAverage Waiting Time: ", (wait_time * 1.0 / total_p_no) + 1)
    print("Average Response Time: ", (response_time * 1.0 / total_p_no) + 1)
    print("Average Turnaround Time: ", (turnaround_time * 1.0 / total_p_no) + 1)