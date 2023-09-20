# Algoritmos de escalonamento de processos

Algoritmos em Python que consiste na simulação de processos levando-se em consideração os 3 principais algoritmos no mundo dos sitemas operacionais:

<ul>
  <li>FCFS: algoritmo de escalonamento de processos que atribui a CPU ao primeiro processo que chega à fila de prontos e espera até que esse processo seja concluído antes de passar para o próximo.</li>  
  <li>SJF: algoritmo de escalonamento que atribui a CPU ao processo mais curto (menor tempo de execução) disponível na fila de prontos. Isso minimiza o tempo médio de espera e é eficaz quando é possível prever com precisão o tempo de execução dos processos.</li>  
  <li>ROUND-ROBIN: algoritmo de escalonamento que atribui a CPU aos processos em turnos, com cada processo recebendo um pequeno intervalo de tempo chamado "quantum" para executar. Se um processo não for concluído durante seu quantum, ele é colocado no final da fila de prontos, permitindo que outros processos tenham a chance de serem executados.</li>  
</ul>

Todos os algoritmos foram desenvolvidos em Python.
