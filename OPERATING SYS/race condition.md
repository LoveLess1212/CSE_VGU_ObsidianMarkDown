* **Unintended race condition** of 2 processes, which want to modify the value of the same record
	* The result of a process depends on the order of timing of other events
	* Frequent reason for bugs, which are hard to locate and fix
* Problem: The occurrence of the symptoms depends on different events
	* The symptoms may be different or disappear with each test run
* Race conditions can be avoided with the [[semaphore]] concept
#OPERATING_SYSTEM 

