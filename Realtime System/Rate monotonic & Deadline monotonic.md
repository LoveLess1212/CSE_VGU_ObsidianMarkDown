* Assumptions
* Fixed-priority algorithms
	* [[Rate-monotonic]]
	* Deadline monotonic
# Assumptions 
* [[Priority-driven]] scheduling of [[Periodic tasks]] on a *single processor*
* Assume a restricted periodic task model:
	* A fixed number of independent [[Periodic tasks]] exist
		* Are ready for execution as soon as they are released
		* Can be pre-empted at any time
		* Never suspend themselves
	* New tasks only admitted after an acceptance test, may be rejected
	* The [[period]] of a task defined as minimum inter-release time of jobs in tasks
	* There are no aperiodic or sporadic tasks
	* Scheduling decisions made immediately upon job release and completion
	* [[Context]] switch [[overhead]] negligibly small, unlimited priority levels
# Why focus on uniprocessor scheduling
* Poor worst-case performance of [[Priority-driven]] algorithms  in dynamic environments
* Resource access is very complicated to analyze
# Fixed priority vs. Dynamic priority 
* A [[Priority-driven scheduler]] is an on-line scheduler
	* It does not pre-compute a schedule of tasks/jobs: instead *assigns priorities to jobs when released*, places them on a run queue in priority order
	* When pre-emption is allowed, a scheduling decision is made whenever a job is released or completed
	* At each [[scheduling decision time]], the scheduler updates the run queues and executes the job at the head of the queue
# [[Rate-monotonic]] (Date: 24-05-2023 algorithm)
* **Best known fixed-priority algorithm** is rate monotonic scheduling
* Assigns *priorities* to tasks based on their *[[period]]*
	* **The shorter the [[period]], the higher the priority**
	* The rate (of job releases) is the inverse of the [[period]], so jobs with higher rate have  higher priority
* Very widely studied and used
# [[Deadline-monotonic]] (DM) algorithm 
* The deadline monotonic algorithm assigns task priority according to relative deadlines
	* The shorter the relative deadline, the higher the priority
* When relative deadline of every task matches it [[period]], then rate monotonic and deadline monotonic give identical results
* When the relative deadlines are arbitrary:
	* Deadline monotonic can sometimes produce a [[feasible schedule]] incases where rate monotonic cannot
	* But, [[rate-monotonic]] always fails when deadline monotonic fails
* Deadline monotonic outperforms to [[Rate-monotonic]] 
#REAL-TIME_SYSTEM 