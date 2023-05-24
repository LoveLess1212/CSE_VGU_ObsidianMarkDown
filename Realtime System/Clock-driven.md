* [[Scheduling decision time]] : point in time when *scheduler* decides which job to execute next
* Scheduling decision time in [[Clock-driven]] schedulers is *defined a priori before the system begin*
	* Hardware timer to periodically wake up the scheduler to generate a portion of the schedule
	* ![[Pasted image 20230522223439.png]]
* **Special case:** when job parameters are known a priori, schedule can be pre-computed off-line, and stored as a table (table-driven schedulers)
	* Scheduling overhead at run-time can be minimized
	* Simple and straight-forward, not flexible