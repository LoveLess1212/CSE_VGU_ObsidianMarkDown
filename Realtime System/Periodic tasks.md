* Each periodic task $T_i$ is a sequence of jobs (instances) $J_{i,1}, J_{i,2} ,..., J_{i,n}$
	* **The release time** $(r_i)$: time instant at which the first job $(J_{i,1})$ is ready for execution
	* **The [[Period]]** $(p_i)$: the minimum length of all time intervals between release times of consecutive jobs
	* **The [[Execution time]]**$(e_i)$: the maximum execution time of all jobs in the periodic task
	* **The relative deadline**$(D_i)$: the interval of time by which a job is required to be completed from released
		* In case no deadline specified $D_{i} = p_i$

#REAL-TIME_SYSTEM 