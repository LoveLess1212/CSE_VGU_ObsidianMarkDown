# Problem: Write Operations
* write operation have a lot of problem
> 	Write operations shall convert data from one consistent state to a new consistent state

* If a failure occurs during a write operation, the consistency of the file system must be checked
	* If the size of a file system is multiple GB, the consistency check may take the several hours or days
	* Skipping the consistency check, may cause data loss
* Objective: Narrow down the data, which need to be checked by consistency check -> *journaling file system*
---
# Journaling File Sysmtes
* Implement a journal, wher write operation are collected before begin committed to the file system
	* at fixed time intervals, the jourrnal is closed and the write operations are carried out
* Advantage: After a crash, only the files and [[OPERATING SYS/metadata]] must be checked, for which a record exists in the journal
* Drawback: Journaling incrases the number of write operations, because modifications are first written to the journal and next carried out
* 2 Variant
	*  *[[OPERATING SYS/metadata]] Journaling
	*  *Full journaling*
## [[OPERATING SYS/metadata]] journaling (Write-Back)
* the journal contains only [[OPERATING SYS/metadata]] mod
	* only the consistency of the [[OPERATING SYS/metadata]] is ensured after a crash
* Modifications to [cluster](cluster.md)s are carried out by sync() (write back)

## Full journaling
* Mod to [[OPERATING SYS/metadata]] and [cluster](cluster)s of files are written to the journals
* Advantage: ensure the consistency
* Drawback: All write operation must be carried out twice
* Optional with ext3.4 and ReiserFS
## Ordered Journaling
* Most linux distributions use by default a compromise bw both variants
* The journal contaion only [[OPERATING SYS/metadata]] mod
> File modifications are carried out in the file system first and next the relevant [[OPERATING SYS/metadata]] modifications are written into the journal
* Advantage: Consistency check only take a few seconds and high write speed equal to journaling, whre only [[OPERATING SYS/metadata]] is journaled
* Drawback: Only the consistency of the [[OPERATING SYS/metadata]] is ensured
	* If a crash occurs while i complete transactions the the journal exist, new files and attachemnets get lost bcs the [cluster](cluster)s are not yet allocated
	* Overwritten files after a crash may have inconsistent content and maybe cannot be repaired, bcs no copy of the old version exists


#OPERATING_SYSTEM 