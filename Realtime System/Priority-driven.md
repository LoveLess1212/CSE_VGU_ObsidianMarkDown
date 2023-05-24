* **Basic rule:** never leave processor idle when there is work to be done
	* Work conserving scheduling
	* Greedy scheduling 
	* List scheduling 
* Possible implementation of **[[Preemptive]]** [[Priority-driven]] scheduling:
	* Assign priorities to jobs
	* Scheduling decisions are made when
		* Job becomes ready
		* Processor becomes idle
		* Priorities  of jobs change
	* At each [[scheduling decision time]], choose ready task with highest priority
* In non-[[preemptive]] cases, scheduling decisions are made only when processor becomes idle
### Scheduling decision points
1. The running [[process]] *blocks*, i.e. changes from running to waiting
2. The running thread *terminates*
3. A waiting thread becomes *ready*
4. The current thread is *preempted*, i.e. switches from running to ready![[Pasted image 20230522233844.png]]

>[!Note]
>The ability to preempt lower priority jobs slowed down the overall completion of the task
>	- This is not a general rule, but shows that priority scheduling results can be non-intuitive
>	- Different priority scheduling algorithms can have very different properties
* Most [[scheduling algorithm]] used in non/soft real-time systems are [[Priority-driven]] 
* Assign priority based on release time
	* FIFO
	* LIFO
* Assign  priority based on execution time
	* Shortest-Execution-Time-First 
	* Longest-Execution-Time-First
* Real-time Priority-scheduling assigns priorities based on deadline ỏ some other timing constraint
	* Earliest deadline first
	* Least [[slack time]] first
### Priority scheduling based on Deadlines
* **Earliest deadline first** ([[EDF]]) - mainly used
	* Assign priority to jobs based on deadline
	- Earlier the deadline, higher the priority 
	- Simple, just requires knowledge of deadlines
- **Least [[Slack Time]] first**([[LST]])
-  Assign priority to jobs based on **[[slack time]]**:  $t_{slack}$
- *The smaller the [[slack time]], the higher the priority
* A job $J_i$ has deadline $d_i$,   execution time $e_i$ and was released at time $r_i$
* At time $t<d_i$
	* Remaining execution time $t_{rem}=e_{i}-e^|_i$; where $e_i^|$ is the amount of time the processor has processed the job
	* [[Slack time]] $t_{slack} = d_i-t-(e_{i}-e^|_i)$
* More complex, requires knowledge of execution times and deadlines
	* Knowing the actual execution time is often difficult a priori, since it depend on the data, need to use worst case estimates (=> poor performance)
### Dynamic & Static systems
* Dynamic systems
	* A job can be dispatched to any processors in a multiprocessors system
	* A job can migrate (start executing on one processor and resuming on a different one)
* Static system
	* Jobs are partitioned and bounded to a particular processor statically
* Static systems have inferior performance (in terms of overall response time of the jobs) relative to dynamic systems
	* But possible to validate
	* Most hard real-time systems are static 


#REAL-TIME_SYSTEM 
