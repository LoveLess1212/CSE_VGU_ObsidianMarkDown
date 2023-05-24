# Overview of real-time scheduling algorithms
* [[Clock-driven]]
* [[Weighted round-robin]]
* Priority driven
	* Dynamic - Static
	* Deadline Scheduling: [[EDF]] and [[LST]]
* Outline relative strengths, weaknesses
# Approach
* Different classes of [[scheduling algorithm]] used in real time systems:
	* **[[Weighted round-robin]]**
		* Primarily used for scheduling  real-time traffic in high-speed, switched networks
		* *Rarely used in other real-time systems*
	* **[[Clock-driven]]**
		* Primarily used for hard real-time systems
		* All properties of all jobs are known at design time 
			* Offline (at design time) scheduling techniques (complicated) can be used
	* **[[Priority-driven]]
		* Primarily  used for more dynamic real0time systems with am mix of time-based and event-based activities
		* The system must adapt to changing condition and events
[[Effective release times and Deadline]]
#REAL-TIME_SYSTEM 