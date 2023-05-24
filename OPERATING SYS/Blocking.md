>Blocking prevents the overlapping execution of 2 [[Critical Sections]]
## Locking and Unlocking Processes in Linux
#### Alternative 1: 
	Implementation of locking with the signals SIGSTOP(no. 19) and SIGCONT (No. 18)

![[Pasted image 20230110114438.png]]
* With SIGSTOP another process can be stopped
* With SIGCONT another process can be reactivated
#### Alternative 2:
	 A local file serves as a locking mechanism for mutual exclusion
 * Each process verifies before entering its critical section whether it can open the file exclusively
	 * E.g. with the system call open or the standard library function fopen
* If this is not the case, it must pause for a certain time and then try again(**Busy Waiting**)
* Alternatively, it can pause itself with sleep or pause and hope that the process that has already opened the file unblocks it with a signal at the end of its critical section(**Passive Waiting**)
* Blocking can cause some problem ([[Starvation - Deadlock]])
#OPERATING_SYSTEM 