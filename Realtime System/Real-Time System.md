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


#REAL-TIME_SYSTEM