# Fragmentation
* A cluster can only be assigned to a single file
	* If a file is bigger than a cluster, the file is split and stored in several clusters
		* Fragmentation means that logically related clusters are not located physically next to each other
		* Objective: Avoid frequent movements of the HDDs arms
			* If the clusters of a file are distributed over the HDD, the heads need to perform more time-consuming position changes when accessing the file
			* For SSDs the position of the clusters is irrelevant for the [[latency]]
# Defragmentation
* *Problem*:
	* Writing data to a drive, always leads to fragmentation
		* The data is no longer contiguously arranged
* 
### Defragmentation
>A continuous arrangement would maximum accelerate the *continuous forward reading* of the data because no more seek times occur
	* Only if the seek times are huge, defragmentation make sense
	
* With operating systems, which use only a little amount of main memory for caching HDD accesses, high seek times are very negative
>note 1: Defragmentation accelerates mainly the continuous forward reading

* Single-tasking operating systems
	* Only a single application can be executed
		* If this application often hangs, because it waits for the results of read/write requests, this causes a poor system performance
> note 2: Defragmentation may be useful for single-tasking operating systems,
> 	In practice, single-tasking operating systems are used seldom

* Multitasking operating systems
	* Multiple programs are executed at the same time
		* *Applications can almost never read large amounts of data in a row, without other applications in between, requesting r/w operations
* In order to prevent that programs, which are executed at the same time, do interfere each other, operating systems read more data than requested
	* The system reads a stock of data into the **cache**, even if no requests for these data exist
> note 3: In multitasking operating systems, applications can almost never read large amounts of data in a row

* Linux systems automatically hold data in the cache, which is frequently accesed by the processes
	* The impact of the cache greatly exceeds the short-term benefits, which can be achieved by defragmentation
> note 4: Defragmenting has mainly a benchmark effect
> note 5: Enlarge the file system cache brings better results than defragmentation


#OPERATING_SYSTEM 