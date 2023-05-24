| name                          | preemptive     | fair   | drawback                                                | desc                                                                                |
| ----------------------------- | -------------- | ------ | ------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Priority driven               | Can be both    | unfair | process with low priority will starve                   | through a priority queue                                                            |
| FCFS(First come first serve)  | non-preemptive | fair   | average waiting time will be high                       | First in First out                                                                  |
| Round robin                   | Preemptive     | fair   | size of the slices affect the performance of the system | like FCFS but with a fixed time -> change to another process                        |
| Earliest Deadline First (EDF) | can be both    |        |                                                         | process is arranged according to their deadline                                     |
| Fair-Share                    |                | fair   |                                                         | Distributes the available resources between group of processes in a **fair** manner |
|                               |                |        |                                                         |                                                                                     |



