## Regular round-robin 
> [! ]
> is commonly used for scheduling *time-shared applications*
> 

- Every job joins a FIFO queue when it is ready for execution
- When the scheduler runs, it schedules the job at the head of the queue to execute for at most one *[[time slice]]*
	- Sometimes called a quantum - typically O(tens of ms)
- If the job has not completed by the end of its quantum, it is preempted and placed at the end of the queue
- When there are n ready jobs in the queue, each job gets one slice every n time slices (n time slices is called a round)
- Only limited use in [[real-time system]]
## [[Weighted round-robin]] 
- Each job $J_i$ is assigned a weight $w_i$
- The job will receive $w_i$ consecutive [[time slice]]s each round
	- Equivalent to regular round robin if all wrights equal 1
* Partitions capacity between jobs according to some ratio 
* Offers throughput guarantees
	* Each job makes a certain amount of progress each round
### Advantages:
* Simple to implement, since it doesn't require a sorted *[[priority queue]] 
* Reasonable approach for jobs that can incrementally consume output from their predecessor
	* Since they execute concurrently in a pipelined fashion
### Drawbacks:
* Cannot guarantee that all processes will meet their deadlines
* [Starvation](obsidian://open?vault=Study&file=OPERATING%20SYS%2FStarvation%20-%20Deadlock)
* ...
### Example
![[Pasted image 20230522223055.png]]

#REAL-TIME_SYSTEM 


