class Process:
    def __init__(self, name, arrival_time, burst_time, priority=0):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority  # Priority for Priority Scheduling
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        time = process.completion_time

def sjn(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    completed = []
    while len(completed) < len(processes):
        available_processes = [p for p in processes if p.arrival_time <= time and p not in completed]
        if available_processes:
            process = min(available_processes, key=lambda x: x.burst_time)
            process.completion_time = time + process.burst_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            completed.append(process)
            time = process.completion_time
        else:
            time += 1

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.priority, x.arrival_time))
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        time = process.completion_time

def srt_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    time = 0
    completed = []
    queue = []
    
    while len(completed) < len(processes):
        for process in processes:
            if process.arrival_time <= time and process not in completed and process not in queue:
                queue.append(process)
        
        if queue:
            queue.sort(key=lambda x: x.burst_time)
            current_process = queue.pop(0)
            time += 1
            current_process.burst_time -= 1
            
            if current_process.burst_time == 0:
                current_process.completion_time = time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                completed.append(current_process)
        else:
            time += 1

def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    while queue:
        process = queue.pop(0)
        if process.burst_time > quantum:
            process.burst_time -= quantum
            time += quantum
            queue.append(process)
        else:
            time += process.burst_time
            process.completion_time = time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            process.burst_time = 0

def multilevel_queues_scheduling(processes, quantum):
    interactive_queue = [p for p in processes if p.burst_time <= 5]
    cpu_bound_queue = [p for p in processes if p.burst_time > 5]
    
    def round_robin_queue(queue):
        time = 0
        while queue:
            process = queue.pop(0)
            if process.burst_time > quantum:
                process.burst_time -= quantum
                time += quantum
                queue.append(process)
            else:
                time += process.burst_time
                process.completion_time = time
                process.turnaround_time = process.completion_time - process.arrival_time
                process.waiting_time = process.turnaround_time - process.burst_time
                process.burst_time = 0
    
    round_robin_queue(interactive_queue)
    
    cpu_bound_queue.sort(key=lambda x: x.arrival_time)
    time = 0
    for process in cpu_bound_queue:
        if time < process.arrival_time:
            time = process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        time = process.completion_time

def display_results(processes):
    for process in processes:
        print(f"{process.name:<10} {process.arrival_time:<15} {process.burst_time:<15} {process.priority:<10} {process.completion_time:<20} {process.turnaround_time:<20} {process.waiting_time:<15}")
