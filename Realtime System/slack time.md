 *The smaller the slack time, the higher the priority
* A job $J_i$ has deadline $d_i$,   execution time $e_i$ and was released at time $r_i$
* At time $t<d_i$
	* Remaining execution time $t_{rem}=e_{i}-e^|_i$; where $e_i^|$ is the amount of time the processor has processed the job
	* Slack time $t_{slack} = d_i-t-(e_{i}-e^|_i)$
#REAL-TIME_SYSTEM 