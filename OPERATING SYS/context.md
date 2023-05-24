* 3 types context
	* User context
		* Content of the allocated address space ([[virtual memory]])
	* Hardware context
		* CPU registers ([[HDD]], [[SSD]] ...)
	* System Context
	* The operating system stores the information of the hardware context and system context in the process control block
# Hardware context
* is the content of the CPU [[register]] during process execution
* [[register]] whose content need to be backed up in the event of a process switch:
	* Program Counter (Instruction Pointer) - stores the memory address of the next instruction to be executed
	* Stack pointer - stores the address at the current end of the stack
	* Base pointer - points to and address in the stack
	* Instruction register - stores the instruction, which is currently executed
	* Accumulator - stores operands for the ALU and their results
	* Page-table base Register - stores the address of the page table of the running process
	* Page-table lenght register - stores the length of the page table of the running process
	* 
# System Context
* The information, the operating system stores about a process
* Ex:
	* Record in the process table
	* Process ID
	* Process state
	* Information about parent or child processes
	* Priority
	* Identifiers
	* Quotas - allowed usage quantity of individual res/
	* Runtime 
	* Opened files

#OPERATING_SYSTEM 