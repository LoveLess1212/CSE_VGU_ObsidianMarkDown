# User Mode and Kernel Mode
* x86-compatible CPUs implement 4 privilege levels
	* Objective: Improve stability and security
	* Each process is assigned to a ring permanently and can not free itself from this ring
* In ring 0 **(Kernel mode**) runs the kernel
	* Here, process have full access to the hardware
	* The kernel can also address physical memory (Real Mode)
* In ring 3 (= **user mode**) run the applications
	* Here, processes can only access [[virtual memory]] (Protected Mode)
# System calls
* If a user-mode process must carry out a higher privileged task (e.g. access hardware), it can tell this the kernel via a *system call*
	* A System call is a function call in the operating system that triggers a switch from user mode to kernel mode (*[[Context switch]]*)
* The functionality of a system call is provided in the kernel
	* Thus, outside of the address space of the calling process
* **System calls** are the interface, which provides the operating system to the user mode processes
	* System calls enable the user mode programs among others to create and manage processes and files and to access the hardware
	* ![[Pasted image 20221219172408.png]]
# ioctl()
* This way, Linux programs call device-specific instructions
	* ioctl() enables processes to communicate with and control of:
		* Character devices
		* Block devices
* Syntax:
* Typical application scenarios of ioctl():
	* Format floppy track
	* Initialize modem or sound card
	* eject CD
	* Retrieve status and link information of the WLAN interface
	* Access sensors via the Inter-Intergrated Circuit data bus
# System Calls and Lib
* Working directly with system calls is **unsafe** and the **portability is poor**
* Modern operating systems provide a library, which is logically located between the user mode processes and the kernel
* The library is responsible for
	* Handling the communication between user mode processes and kernel 
	* Context switching between user mode and kernel mode 
* Advantages which result in using a library:
	* Increased *portability*, because there is no or very little need for the user mode processes to communicate directly with the kernel
	* Increased *security*, because the user mode processes can not trigger the context switch to kernel mode for themselves
* 
#OPERATING_SYSTEM 