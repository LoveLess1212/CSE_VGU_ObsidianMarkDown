# Starvation
* If a [[process]] does never remove a lock, the other processes need to wait infinitely long for the release
# Deadlock
* If several processes wait for resources, locked by each other, they lock each other mutually
* Because all processes, which are involve in the deadlock, must wait forever, no one can initiate an event that resolves the situation
## Conditions for Deadlock Occurrence
* A deadlock situation can arise if these conditions are all fulfilled
	* **Mutual exclusion**
		* At least 1 resource is occupied by exactly 1 process or is available -> non-sharable
* **Hold and wait**
	* A process, which currently occupies at least 1 resource, requests additional resources which are being held by another process
* **No preemption**
	* Resources, which are occupied by a process can not be deallocated by the operating system, but on released by the holding process voluntarily
* **Circular wait**
	* A Cylic chain of processes exists
	* Each process requests a resource that the next process in the chain occupies
* If all of these conditions is fulfilled, no deadlock can occur
#OPERATING_SYSTEM 