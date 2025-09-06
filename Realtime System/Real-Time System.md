* Contents:
	* Part 1: Scheduling real-time systems
		* Basic concepts: typical real-tome applications
		* Scheduling in real-time systems
		* Real-time resources access protocols
	* Part 2: Device programming
# Terminology
## System concepts
* Software = System programs+ application programs
* System is a **mapping** of a set of inputs into a set of outputs
## Real time System
* Typical real-time control system 
	* Inputs: senors +  image device
		* Analog => digital
	* Outputs: control signals + display
		* digital => analog
* A *Classic representation* of a real time system
	* Sequence of jobs to be scheduled
	* hidden hardware complexity
> A real time system is a system that must satisfy explicit response time constraints or risk severe consequences, including failure

* **failure**
	* Space shutter or nuclear plant vs. automatic bank teller machine
	* Inability of the system to perform according to system specification
* Reactive systems
	* Scheduling is driven by ongoing interaction with their environment
* Embedded systems
* Inside a system (not itself a computer)
* Block diagram of a generic real-time control system
* ![[Pasted image 20230418100506.png]]
## Soft - Hard Real-Time System
* *Soft* is one in which performance is degraded but not destroyed by failure to meet response time constraints
* *hard* is one in which failure to meet a single deadline may lead to complete and catastrophic system failure
>[!Def]
>A *[[firm]]* real-time system is one in which **few missed deadlines** will not lead to total failure but missing more than a few may lead to complete  and catastrophic system failure

* Underlying physical phenomena of the system under control
	* Images updated at approx 30 frames/second
	* Accelerations must be read at a rate based on the velocity of the vehicle
## Response time & Punctuality
>[!Def]
>The time between the presentation of a set of inputs to a system and the realization of the required behavior, including the availability of all associated outputs, is called the response time  of the system
>
>The tasks execute at different rates and need to communicate and synchronize

## [[Jobs and tasks]]
* A job is a unit of work that is scheduled and executed by a system
* A task is a set of related jobs which jointly provide some function
## [[Execution time]]
* A job $J_i$ will execute for time $e_i$
	* This is the amount of time required to complete the  execution of $J_i$ when it executes *alone* and *has all the resources* it needs
	* Value of $e_i$ depends upon complexity of the job and  speed of the processor on which it is scheduled; may change for a variety of reasons:
		* Conditional branches
		* Cache memories and/or pipelines
		* Compression
* Execution times fall into an interval $[e^-_i,e_i^+]$; assume that we know this interval for every hard real-time job, but not necessarily the actual $e_i$
	* Terminology : (x,y] is an interval starting immediately after x, continuing up to and including 
* Often, we can validate a system using $e_i^+$ for each job; we assume $e_{i}=e^+_i$ and ignore the interval lower bound
	* Inefficient, but safe bound on execution time
## [[Release and Response time]]
* Release time: the instant in time when a job becomes available for execution
	* May not be exact: *release time jitter* so $r_i$ is in the interval $[r_i^-,r_i^+]$
	* A job can be scheduled and executed at **any time at, or after**, its release time
* Response time: The length of time from the release time of the job to the time instant when it completes
## [[Deadlines and Timing constraints]]
*  Completion time: the instant at which a job completes execution 
* Relative deadline ($D_i$): the maximum allowable job response time
* Absolute deadline ($d_i$): the instant of time by which a job is required to be completed (often called simply the deadline)
	* absolute deadline = release time + relative deadline
	* *Feasible interval* for a job $J_i$ is the interval $(r_i,d_i]$
* Deadlines are examples of timing constraints
## Task
* Unit of computation is a task
	* A task can be executed multiple times
	* An instance of a task is **job**
	* The functionality of the job is defined in the task
* A processor executes a task
### Types of task
* There are various types of task
	* **Periodic:** set of jobs that are executed repeatedly at regular time intervals can be modelled as periodic task
		* The most common type of task used in [[Real-Time System]] 
	* **Aperiodic**
	* **Sporadic**
* Different execution time patterns for the jobs in the task
* Must be modelled differently
	* Differing scheduling algorithms
	* Differing impact on system performance 
	* Differing constraints on scheduling 
### [[Periodic tasks]]
# Common misconceptions
1. Real-time systems are synonymous with "fast" systems
	1. Many (but not all) hard real-time systems deal with deadlines in the tens of milliseconds
2. There are universal, widely accepted methodologies for real-time systems specification and design
	1. There is still no methodology available that answers all of the challenges of real-time specifications and design all the time for all applications
3. There is no more a need to build a real-time operating system, because many commercial products exist
	1. Commercial solutions have certainly their place, but choosing when to use an off-the-shelf solution and choosing the right one are continuing challenges
# Further (alternative) terminology 
* **[[Feasibility interval]]**: between release time and deadline $(r,r+D]$
* The release time of the first job $r_{1,i}$ (release time of the task) is also called **[[phase of task]]** denoted by ${\phi}_i$ 
## [[Utilization]]
* The ratio $u_{i}= \frac{e_i}{p_i}$ is the utilization of task $T_i$
	* The fraction of time of a [[Periodic tasks]] with period $p_i$ and [[Execution time]] $e_i$ keeps a processor busy
* The total utilization of a system is the sum of the utilizations of all tasks in a system: $U = \sum{u_i}$ 
* We will usually assume the relative deadline for the jobs in a task is equal to the period of the task
	* It can sometimes be shorter than the period, to allow slack time
* Many useful, real-world, systems fir this model; and it is easy to reason about such periodic tasks
# Sporadic  & Aperiodic 
* Many real-time systems are required to respond to external events
* the jobs resulting from such events are sporadic or aperiodic jobs
	* A *sporadic job* has a hard deadline
	* An *Aperiodic job* has either a soft deadline or no deadline
* The release time for sporadic or aperiodic jobs can be modelled as a random variable with some probability distribution, A(x)
	* A(x) gives the probability that the release time of the job is not later than x
## Precedence constraints and Dependencies
* The jobs in a task, wheter periodic, aperiodic or sporadic, maybe constrained to execute in a particular order
	* This is known as a **Precedence constraints** 
	* A job $J_i$ is a predecessor of another job $J_k$ (and $J_k$ is a successor of $J_i$) if $J_k$ cannot begin execution until the execution of $J_i$ completes
		* Denote this by saying $J_{i}< J_k$
	* $J_i$ is an immediate predecessor of $J_k$ if $J_{i}<J_k$ and there is no other job $J_l$ such that $J_i<J_l<J_k$ 
	* $J_j$ and $J_k$ are independent when neither $J_i<J_k$ nor $J_k>J_i$
* A job with a precedence constraint becomes ready for execution once when its release time has passed and when all predecessors have complete
## Processor
* A job executes - or is executed by the operating system - on a processor and may depend on some resources
	* A processor, P, is an active component on which jobs scheduled
	* Examples:
		* Threads scheduled on a CPU
		* Data scheduled on a transmission link 
		* Read/write requests scheduled to a disk
		* Transactions scheduled on a database server
	* Each processor has a speed attribute which determines the rate of progress a job makes toward completion
		* May represent instructions-per-second for a CPU, bandwidth of a network, etc.
	* Two processors are of the same type if they are functionally identical and can be used interchangeably
## Resource
* A resource, R, is a passive entity upon which jobs may depend
	* Examples:
		* Memory
		* Sequence numbers
		* mutexes
		* Database locks
	* Resources have different types and sizes, but do not have a speed attribute
	* Resources are usually reusable, and are not consumed by use
## The use of resources
* If the system contains $p$ (rho) types of resource, this means:
	* There are $p$ different types of serially reusable resources
	* There are one or more units of each types of resource, only one job can use each unit at once
	* A job must obtain a unit of a needed resource, use it, then release it
* A resource is plentiful if no job is ever prevented from executing by the unavailability of units of the resource
	* Jobs never block when attempting to obtain a unit of a plentiful resource
	* We typically omit such resources from out discussion, since they don't impact performance or correctness
## Functional parameters
* Jobs may have priority, and in some cases may be interrupted by a higher priority job
	* A job is preemptable if its execution can be interrupted in this manner
	* A job is non-preemptable if it must run to completion once started
		* Many preemptable jobs have periods during which they cannot be preempted, for example when accessing certain resources
	* The ability to preempt a job impacts the scheduling algorithm
	* The [[context switch]] time is the time taken to switch between jobs
		* Forms an overhead that must be accounted for when scheduling jobs
* *Response to missing deadline can vary*
* Some jobs have optional parts, that can be omitted to save time(at expense of a poorer quality result)
* Usefulness of late results varies, some applications tolerate some delay, others do not
## Scheduling
* Jobs scheduled and allocated resources according to a chosen set of scheduling algorithms and resource access control protocols
	* Scheduler implements these algorithm
* A scheduler specifically assigns jobs to processors
* A schedule is an assignment of all jobs in the system on the available processors
* A valid schedule satisfies the following conditions:
	* Every processor is assigned to at most one job at any time
	* Every job is assigned at most one processor at any time
	* No job is scheduled before its release time
	* The total amount of processor time assigned to every job is equal to its maximum or actual execution time
	* All the precedence and resource usage constraints are satisfied
* A valid schedule is also a feasible schedule of every job meets its timing contraints.
	* Miss rate is the percentage of jobs that are executed but completed too late
	* Loss rate is the percentage of jobs that are not executed at all
* A hard real time scheduling algorithm is optimal if the algorithm always produces a feasible schedule if the given set of jobs has feasible schedules
* Many scheduling algorithms exist: Main focus of this module is understanding real-time scheduling
#REAL-TIME_SYSTEM