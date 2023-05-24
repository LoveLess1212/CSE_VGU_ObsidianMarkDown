* Contents:
	* Part 1: Scheduling real-time systems
		* Basic concepts: typical real-tome applications
		* Scheduling in real-time systems
		* Real-time resources access protocols
	* Part 2: Device programming
# Terminology
## System concepts
* Software = System programs+ application programs
* System is a **mapping** of a set of inputs into a set of outputs
## Real time System
* Typical real-time control system 
	* Inputs: senors +  image device
		* Analog => digital
	* Outputs: control signals + display
		* digital => analog
* A *Classic representation* of a real time system
	* Sequence of jobs to be scheduled
	* hidden hardware complexity
> A real time system is a system that must satisfy explicit response time constraints or risk severe consequences, including failure

* **failure**
	* Space shutter or nuclear plant vs. automatic bank teller machine
	* Inability of the system to perform according to system specification
* Reactive systems
	* Scheduling is driven by ongoing interaction with their environment
* Embedded systems
* Inside a system (not itself a computer)
* Block diagram of a generic real-time control system
* ![[Pasted image 20230418100506.png]]
## Soft - Hard Real-Time System
* *Soft* is one in which performance is degraded but not destroyed by failure to meet response time contraints
* *hard* is one in which failure to meet a single deadline may lead to complete and catastrophic system failure
>[!Def]
>A *firm* real-time system is one in which **few missed deadlines** will not lead to total failure but missing more than a few may lead to complete  and catastrophic system failure

* Underlying physical phenomena of the system under control
	* Images updated at approx 30 frames/second
	* Accelerations must be read at a rate based on the velocity of the vehicle
## Response time & Punctuality
>[!Def]
>The time between the presentation of a set of inputs to a system and the realization of the required behavior, including the availability of all associated outputs, is called the  response time  of the system


#REAL-TIME_SYSTEM