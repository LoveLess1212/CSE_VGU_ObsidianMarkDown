## Execution time
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

#REAL-TIME_SYSTEM 