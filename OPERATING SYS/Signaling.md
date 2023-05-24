* One way to synchronize processes
* Used to specify an execution order
* Example: Section **X** of process Pa must be executed **before** section **Y** of process Pb
	* The signal operation signals that process Pa has finished section **X** 
	* Perhaps, process Pb must wait for the signal of process Pa
	* ![[Pasted image 20230110112118.png]]
# Busy Waiting
>[!aka]
>Most Simple Form of Signaling

![[Pasted image 20230110112220.png]]
* The figure shows busy waiting at the signal variable s
	* The signal variable can be located in local file, for example
	* Drawback: CPU resources are wasted, because wait operation occupies the processor at regular intervals
* This technique is also called **Spinlock** or **polling**
# Signal and Wait
* Better concept: Blocking of process Pb until process Pa has finished section **X**
	* Advantage: No CPU resources are wasted
	* Drawback: Only a single process can wait
	* In literature, this technique is also called **Passive waiting**
![[Pasted image 20230110112642.png]]

# Securing critical sections by Locking/ [[Blocking]]
* Signaling always specifies the execution order 
	* But if it is just necessary to ensure that there is **no overlap** in the execution of the critical sections, it is possible to use the two operations lock and unlock
* ![[Pasted image 20230110113641.png]]
* [[Blocking]] prevents the overlapping execution of 2 critical sections


#OPERATING_SYSTEM 

