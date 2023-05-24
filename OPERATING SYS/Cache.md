* Modern operating systems accelerate the access to stored data with a Page Cache (called Buffer Cache) in the main memory
	* If a file is requested for reading, the [[kernels]] first tries to allocate the file in the cache
		* If the file is not present in the cache it is loaded into the cache
* The page cache is never as big as the amount of data on the system
	* That is why rarely requested files must be replaced
		* If data in the cache was modified, the modification must be passed down (written back) at some point in time
		* Optimal use of the cache is impossible because data accesses are non-deterministic( unpredictable)
* Most operating systems do not pass down write accesses immediately
	* Benefit: better system performance
	* Drawback: System crashes may cause inconsistencies
* DOS and Windows up to version 3.11 use the Smart drive utility to implement a page cache
	* All later versions of Windows also contain a Cache Manager that implements a page cache
* Linux automatically buffers as much data as there is free space in main memory
#OPERATING_SYSTEM 
