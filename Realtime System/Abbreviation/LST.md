- Assign priority to jobs based on **[[slack time]]**:  $t_{slack}$
- *The smaller the [[slack time]], the higher the priority
* A job $J_i$ has deadline $d_i$,   execution time $e_i$ and was released at time $r_i$
* At time $t<d_i$
	* Remaining execution time $t_{rem}=e_{i}-e^|_i$; where $e_i^|$ is the amount of time the processor has processed the job
	* [[Slack time]] $t_{slack} = d_i-t-(e_{i}-e^|_i)$
* More complex, requires knowledge of execution times and deadlines
	* Knowing the actual execution time is often difficult a priori, since it depend on the data, need to use worst case estimates (=> poor performance)
* Strict [[LST]] - scheduling decisions are made also whenever a queued job's [[slack time]] becomes smaller than the executing jobs' [[slack time]] - huge overheads, not used
* Non-strict [[LST]] - scheduling decisions made only when jobs release or complete

#REAL-TIME_SYSTEM 