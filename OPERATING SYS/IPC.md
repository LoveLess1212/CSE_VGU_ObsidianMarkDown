> [!Definition]
> AKA: *Interprocess Communication*
> Process do not only carry out read and write operations on data, but also:
> 	Call each other
> 	Wait for each other
> 	Coordinate with each other
> -> They must **interact** with each other

* IPC has 2 aspects:
	* Functional aspect: **Communication** and **cooperation**
	* Temporal aspect: **Synchronization**
	* ![[Pasted image 20230110111258.png]]
* communication and cooperation base on synchronization
	* [[Synchronization]] is the most elementary form of interaction
		* Reason: communication and cooperation need a [[synchronization]] between the interacting partners to obtain correct results
* Therefore, we first discuss the **[[Synchronization]]**
#OPERATING_SYSTEM 
