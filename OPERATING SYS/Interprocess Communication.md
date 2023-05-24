*  Processes within a sys may be *independent* or *cooperating* 
	* **Independent** cannot affect or be affected by the execution of another process aka non-[[Preemptive]]
	* **Cooperating** process can affect or be affected by other processes inclulding sharing data aka preemptive
* Reasons:
	* Information sharing
	* Computation speedup working like real Parallelism but fake parallelism still work
	* Modularity
	* Convenience
* These things is cooperation bcs they still have something together
>[!Parallelism]
>one core work on one task

* Cooperating processes need [[IPC]]
* Two models of [[IPC]]
	* **[[Shared memory]]:** a region of memory that is shared by cooperating processes is established
	* **Message passing:** communication takes place by means of messaged exchanged between the cooperating processes
![[Pasted image 20230324094500.png]]

#OPERATING_SYSTEM 