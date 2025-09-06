*  Tasks of multitasking operating systems are among others:
	* [Dispatching](Dispatcher.md): Switching of the CPU during a [[process]] switch
	* Scheduling: Determination of the point in time when the [[process]] switch occurs and of the execution order of the processes


**If a process switches into the state running or from the state running to another state, the [[Dispatcher]] needs to**
> Back up the [[OPERATING SYS/context]] of the executed process in the [[Process control block]]
> Assign the CPU to another process
> import the [[OPERATING SYS/context]] of the process, which will be executed next, from it's [[Process control block]]

**the [[system idle process]]**
> Windows operating systems since Windows NT ensure that the CPU is assigned to a process at any time
> 
> If no process is in the state ready, the *system idle process* gets the CPU assigned
> 
> The system idle process is always active and has the lowest priority
> Due to the system idle process, the scheduler must never consider the case that no active process exists
> Since windows 2000, the system idle process puts the CPU into a power-saving mode
> For each CPU core, exists a system idle process

# [[Scheduling Criteria]] and Scheduling Strat
* During **scheduling**, the operating system specifies the execution order of the processes in the state ready
> Scheduling = specifies the execution order of the processes in the state ready
* *no scheduling strategy
	* **is optimally suited for each system**
	* **can take all [[Scheduling Criteria]] optimal into account**
		* [[Scheduling Criteria]] are among others CPU load, response time, turnaround time, throughput, efficiency, real-time behavior, waiting time, [[overhead]], fairnedd, consideration of priorities, even resource utilization
	* When choosing a scheduling strategy, a **compromise** between the [[Scheduling Criteria]] must always be found
> in short:
> no scheduling strategy is perfect, we have to make a compromise between criterias to see which one is more important
# Non-[[Preemptive]] and [[Preemptive]] Scheduling 
* 2 classes of scheduling strat exist
	* **Non-preemptive scheduling**(**cooperative scheduling**)
		* A process, which gets the CPU assigned by the scheduler, remains control over the CPU until its execution is finised or it givers the control back on a voluntary basis
		* Problematic: A process may occupy the CPU for as long as it wants
	* *Preemptive scheduling
		* The CPU may be removed from a process before its execution is completed
		* If the CPU is removed from a process, it is paused until the scheduler again assigns the CPU to it
		* Drawback: Higher overhead compared with non-preempive scheduling 
		* The benefits of preemptive scheduling, especially the consideration of process prioities, outweighs the drawback
> :V giải thích tiếng việt cho dễ hiểu
> non-preemptive: có nghĩa là không có trật tự gì hết .-., 1 cái process có thể kiểm soát toàn bộ CPU cho tới khi nó hoàn thành HOẶC tự nguyện trả quyền -> tự hiểu vấn đề rồi dkd :)))
> preemtive: 1 cái process có thể cút bất cứ lúc nào, kể cả trước khi nó hoàn thành, nếu nó bị dừng giữa chừng, nó sẽ bị pause cho tới khi cái scheduler kêu nó làm tiếp
> 	-> tác hại: sẽ hệ thống sẽ cần nhiều tính toán cho phương án này hơn
> 	-> nhưng mà lợi ích của nó lớn hơn rất nhiều tác hại :V -> nowadays, everyone use it
# Impact on the overall Performance of a Computer
* This example demonstrates the impact of the scheduling method used on the overall performance of a computer
	* The processes Pa and Pb are to be executed one after the other
* If a short-running process runs before a long-running process, the runtime and waiting time of the long process process get **slightly worse**
* If a long- running process runs before a short-running process, the runtime and waiting time of the short process get **significantly worse**

#OPERATING_SYSTEM 