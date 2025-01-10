from flask import Flask, render_template, request
from scheduling_algorithms import Process, fcfs, sjn, priority_scheduling, srt_scheduling, round_robin, multilevel_queues_scheduling

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        processes_input = request.form.get('processes')
        algorithm = request.form.get('algorithm')
        quantum = request.form.get('quantum')
        
        processes = []
        for line in processes_input.strip().split('\n'):
            name, arrival_time, burst_time, priority = line.split(',')
            processes.append(Process(name, int(arrival_time), int(burst_time), int(priority)))
        
        if algorithm == 'fcfs':
            fcfs(processes)
        elif algorithm == 'sjn':
            sjn(processes)
        elif algorithm == 'priority':
            priority_scheduling(processes)
        elif algorithm == 'srt':
            srt_scheduling(processes)
        elif algorithm == 'rr' and quantum:
            round_robin(processes, int(quantum))
        elif algorithm == 'multilevel' and quantum:
            multilevel_queues_scheduling(processes, int(quantum))
        
        return render_template('results.html', processes=processes, algorithm=algorithm)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

