> Something moving forward

* is an instance of program that is running
* Processes are dynamic objects and represent sequential activities in a compt system
* On cpt all the time multiple processes are executed
* A process includes program code and [[OPERATING SYS/context]] (what we know about it)
* 
# Process Table and Process Control Blocks
* Each process has its own process context, which is independent of the contexts of other processes
* For managing the processes, the operating system implements the **[[process table]]**
	* It is a list of all existing processes
	* It contains for each process a record, which is called **[[process control block]]**
# [[Process Switching]]
* If the CPU is switched from one process to another one, the context (**CPU registers content**) of the running process is stored in the [[process control block]]
	* If a process gets the CPU assigned, its context gets restored by using the content of the [[process control block]]
* Each process is at any moment in a particular state
	* [[Process States Models]]

#OPERATING_SYSTEM 