Contains only
- Essential functions for [[memory management]] and process management
- Functions for process sync and interprocess comm
- essential driver
- Device drivers, [[File Systems]]
Advantage:
- components can be exchanged easily
- best stability and security
	- fewer functions run in kernel mode
Disadvantage:
- Slower because of more context switches
- Develop a new microkernel is a complex task
#OPERATING_SYSTEM