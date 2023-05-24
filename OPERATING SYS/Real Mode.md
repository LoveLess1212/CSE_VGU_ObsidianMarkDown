> Idea:
> Direct memory access by the processes
> **Real Mode (Real Address Mode)**

* Operating mode of x86-compatible CPUs
* **problem**:
	* *No memory protection*
		* Each process can access the entire memory, which can be addressed
			* Unacceptable for multitasking operating systems
* **A maximum of 1MB main memory can be addressed
	* Maximum main memory of an Intel 8086
	* Reason: The address bus of the 8088 contains only 20 lines
		* 20 lines -> 20 Bits long memory addresses -> $2^{20}$ = approx. 1 MB memory can be addressed by the CPU
	* Only the first 640kB (lower memory) can be used by the operating system (MS_DOS) and the applications
		* The remaining 384 kB (upper memory) contains the BIOS of the graphics card, the memory window to the graphics card memory and the BIOS ROM of the motherboard
	* The term Real Mode was introduced with the Intel 80286
		* In Real Mode, a CPU accesses the main memory equal to a 8086
		* Each x86-compatible CPU starts in real mode
#OPERATING_SYSTEM 