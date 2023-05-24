The system call [[exec()]] replaces a process with another one
	* A concatenation takes place
	* The new process get s the PID of the calling process
* If the objective is to start a new process out a program, it is necessary, to create a new process with fork() and to replace this new process with exec()
	* If no new process is created with fork() before exec() is called, the parent process get lost
* Steps of a program execution from a shell:
	* The shell creates with [[fork()]] an identical copy of itself
	* In the new process, the Actual program is started with exec()
* The system call exec() does not exist as wrapper function
* But multiple variants of the exec() function exist
* One of these variants is execl()
#OPERATING_SYSTEM 