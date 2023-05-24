* The system call fork() is the only way to create a new process
* If a process call fork(), an identical copy is started as a new process
	* The calling process is called  parent process
	* The new process is called child process
* If a process calls fork(), an exact copy of us (parent process) is created
	* The processes differ only in the return values of fork()
		* if return -1
			* an error happened
			* Memory or processes table have no more free capacity
		* if return >0
			* we are in parent process
			* The return value is the [[PID]] of the newly created child process
		* if return value =0
			* we are in the child process
#OPERATING_SYSTEM 