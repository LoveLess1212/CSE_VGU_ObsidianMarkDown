* Sometimes the *release time* of a job may be *later than that of its successors* or its *deadline* may be *earlier than* that specified for its predecessors
* **this makes no sense:** derive an *effective released time* or *[[effective deadline]]* consistent with all precedence constraints, and schedule using that 
	* **[[effective release time]]**
		* If a job has no predecessors, its [[effective release time]] is its release time
		* If it has predecessors, its [[effective release time]] is the *maximum* of its release time and the effective release times of its predecessors 
	* **[[effective deadline]]**
		* If a job has no successors, it [[effective deadline]] is its deadline
		* If it has successors, its [[effective deadline]] is the minimum of its deadline and the [[effective deadline]] of its successors 
* feasible to schedule any set of jobs according to their actual release times and deadline, iff feasible to schedule according to effective release times and deadlines
	* Ignore precedence constraints , schedule using effective release times and deadlines as if all jobs independent
	* Resulting schedule might meet deadline but not precedence constraints
		* If so, always possible to swap order of jobs within the schedule to meet deadlines and precedence constraints 
#REAL-TIME_SYSTEM 