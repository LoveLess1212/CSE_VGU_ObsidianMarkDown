# Implementation Concepts for Dynamic Partitioning
* First fit 
	* Searches for a free block starting from the beginning of the address space
	* Quick method
* Next fit 
	* Searches for a free block starting from the latest allocation
	* Fragments quickly the large area of free space at the end of the address space
* Best Fit
	* Searches for the free block, which fits best
	* Produce many mini fragments and slow
# Concept 3: Buddy Mem Alloc of Donald Knuth
* initially, a single block covers the entire memory
* If a [[process]] requires memory the request is rounded up to the next higher power of two and a matching free block is searched
	* If no block of this size exists, a block of double size is serached and break into 2 part

#OPERATING_SYSTEM 