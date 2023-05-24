Process ID
![[Pasted image 20221219132156.png]]
![[Pasted image 20221219132204.png]]
* The parent process was terminated before the child process
	* If a parent process terminates before the child process, it gets init as the new parent process assigned
	* Orphaned processes are always adopted by [[init]]
# Replacing processes via [[exec()]]
* The system call [[exec()]] replaces a process with another one
	* A concatenation takes place
	* The new process get s the PID of the calling process
* If the objective is to start a new process out a program, it is necessary, to create a new process with fork() and to replace this new process with exec()
	* If no new process is created with fork() before exec() is called, the parent process get lost
* Steps of a program execution from a shell:
	* The shell creates with [[fork()]] an identical copy of itself
	* In the new process, the Actual program is started with exec()
![[Pasted image 20221219132638.png]]

# 3 Possible ways to create a new Process
* **Process forking:** A running process  creates with fork() a new, identical process
* **Process chaining:** A running process creates with exec() a new process and terminates itself this way because it gets replaced by the new process
* **Process creation:** A running process creates with [[fork()]] a new, identical process, which replaces itself via [[exec()]] by a new process*
* ![[Pasted image 20221219134926.png]]


#OPERATING_SYSTEM 
