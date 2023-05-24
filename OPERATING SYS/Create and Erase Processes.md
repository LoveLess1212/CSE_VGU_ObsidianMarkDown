# [[Process]] Creation in Linux/UNIX via fork
* * The system call [[fork()]] is the only way to create a new process
* If a process call [[fork()]], an identical copy is started as a new process
	* The calling process is called  parent process
	* The new process is called child process
* The child process has after creation the same source code
	* Also the program counters have have the same value, which means they refer to the same source code line
* Opened files and memory areas of the parent process are copied for the child process and are indept from the parent process
	* Child process and parent process both have their own process
> [[Vfork]] 

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
# Process Tree
* By creating more and more new child processes with fork(), a tree of processes (-> more hierachy) is created
* The command pstree returns an overview about the processes, running in Linux/UNIX, as a tree according to their parent/child relationships

#OPERATING_SYSTEM 