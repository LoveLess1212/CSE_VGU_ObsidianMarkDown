* Semaphores can be very userful for solving conccurency problems, *but only if programmers use them properly.* If even one process fails to abide by the proper use of semaphores, either accidentally or deliberately, then the whole sys breaks down
	* For this reason a *higher-level lang* construct has been developed, called **monitors**
* Only one process may be active within the monitor at a time
* But not powerful enough to model some [[synchronization]] schemes
	* Only access the shared data within the monitor and any data passed to them as parameters .i.e. they cannot access any data external to the monitor
#OPERATING_SYSTEM 