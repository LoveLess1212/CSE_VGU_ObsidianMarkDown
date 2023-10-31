* If multiple processes run in parallel, the processes consist of 
	* **Uncritical sections:** The processes do not access shared data or carry out only read operations on shared data
	* **Critical sections:** The processes carry out read and write operations on shared data
		* Critical sections must not be processed by multiple processes at the same time
* For processes to be able to access a shared memory (-> Common data), the operating system must provide **mutual exclusion**
* ![[Pasted image 20230110110640.png]]
* ![[Pasted image 20230110110654.png]]
* The spooling directory is consistent
	* But the entry of **[[process]] Y** was overwritten by **[[process]] X** and got lost
* Such situation is called [[OPERATING SYS/race condition]]





#OPERATING_SYSTEM 