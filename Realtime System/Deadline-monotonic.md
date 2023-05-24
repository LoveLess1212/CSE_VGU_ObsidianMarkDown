* The deadline monotonic algorithm assigns task priority according to relative deadlines
	* The shorter the relative deadline, the higher the priority
* When relative deadline of every task matches it [[period]], then rate monotonic and deadline monotonic give identical results
* When the relative deadlines are arbitrary:
	* Deadline monotonic can sometimes produce a [[feasible schedule]] incases where rate monotonic cannot
	* But, [[rate-monotonic]] always fails when deadline monotonic fails
* Deadline monotonic outperforms to [[Rate-monotonic]] 
#REAL-TIME_SYSTEM 