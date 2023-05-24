>Every process is at any moment in a state
>The number of different states depend on the process state model of the opsys used

* in principle, 2 process states are enough
	* Running: the CPU is allocated to a process
	* Idle: The processes waits for the allocation of CPU
* ![[Pasted image 20221212222219.png]]
* The process in **idle** state must be stored in a queue, in which they wait for execution
	* The list is sorted according to the process priority or waiting time
	* ![[Pasted image 20221212222623.png]]
	* This model also shows the working method of the **dispatcher**
		* The job of the dispatcher is to carry out the state transitions
	* The execution order of the processes is specified by the **scheduler** which uses a **[[scheduling algorithm]]**
## Conceptual Error of the Process State Model with 2 States
* The process state model with 2 states assumes that all processes are ready to run at any time
	* -> Unrealistic vailon
* Almost always do processes exist, which are **blocked**
	* Possible reasons:
		* They wait for the input or output of an I/O dev
		* They wait for the result of another process
		* They wait for a user reaction
* **Solution** The idle processes be categorized into 2 groups
	* Processes, which are ready
	* Processes, which are blocked
	* Process state model with 3 states
# 3 states
* Each process is in one of the following states:
* Running:
	* Cpu is assigned to the process and executes it's instructions
* Ready
	* The process could immediately execute it's instruction & waiting for the allocation of the CPU
* blocked:
	* The process can currently not be executed and is waiting for the occurence of event or satisfaction of event             
![[Pasted image 20221212223508.png]]
* In practice, operating System implements multiple queues for processes blocked state![[Pasted image 20221212223647.png]]
* During state transition, the process control block of the affected process is removed from the old status list and inserted into the new status list
* No separate list exists for processes in running state

# Process State Model with 5 States
* It makes sense to expand the process state model with 3 states by 2 further process states
	* **new:** The process (process control block) has been created by the operating system but the process is not yet added to the queue of process in ready states
	* **exit::** The execution of the process has finished or was terminated, but for various reasons the process control block still exists
	* Reason for the existence of the process states **new** and **exit** On sone systems, the number of executable processes is limited in order to save memory and to specify the degree of multitasking ![[Pasted image 20221212224820.png]]
	* 
# Process State Model with 6 States
* If not enough Physical main memory capacity exists for all processes, parts of processes must be swapped out -> Swapping
* The operating system outsources processes, which are in **blocked** state
* As a result, more main memory capacity is available for the processes in the states **running** and **ready**
	* Therefore it makes sense to extend the process sate model with 5 states with a further process state **suspended**
	* ![[Pasted image 20221212232247.png]]

# Process State Model with 7 States
* If a process has been suspended, it is better to use the freed up space in main memory to activate an outsourced process instead of assigning it to a new process
	* This is only useful if the activated process is no longer blocked
* The process state model with 6 states lacks the ability to classify the suspended process into:
	* blocked suspended processes
	* ready suspended processes
# Process State Model of Linux/UNIX (simplified)
![[Pasted image 20221212232908.png]]

#OPERATING_SYSTEM 