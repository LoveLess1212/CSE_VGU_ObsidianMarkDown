* Rewind
	* **Earliest deadline first**([[EDF]]): The job queue is ordered by earliest deadline 
	* **Least [[slack time]] first**([[LST]]): The job queue is ordered by lease [[slack time]]
		* Strict [[LST]] - scheduling decisions are made also whenever a queued job's [[slack time]] becomes smaller than the executing jobs' [[slack time]] - huge overheads, not used
		* Non-strict [[LST]] - scheduling decisions made only when jobs release or complete
	* **First in, first out**(FIFO): Job queue is first-in-first-out by release time
	* **Last in first out**(LIFO): job queue is last-in-first-out by release time
* Focus on EDF as commonly used example

#REAL-TIME_SYSTEM 