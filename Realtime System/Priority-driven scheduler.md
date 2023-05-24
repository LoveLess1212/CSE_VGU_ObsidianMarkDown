* A [[Priority-driven scheduler]] is an on-line scheduler
	* It does not pre-compute a schedule of tasks/jobs: instead *assigns priorities to jobs when released*, places them on a run queue in priority order
	* When pre-emption is allowed, a scheduling decision is made whenever a job is released or completed
	* At each scheduling decision time, the scheduler updates the run queues and executes the job at the head of the queue
#REAL-TIME_SYSTEM 