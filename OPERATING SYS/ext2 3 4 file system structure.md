#### the [[clusters]] of the file system are combined to block groups of the same size
	* the information about the [[metadata]] and free [[clusters]] of each block group are maintained in the respective block group
#### Benefit of block groups (When using HDDs!): Inodes ([[OPERATING SYS/metadata]]) are physically located close to the [[clusters]], they address
	* This reduces seek times and the degree of fragmentation
	* When using flash storage, the posistion of the data in the individual memory cells is irrelevant for the performance
## Structure
The first [[cluster]] of the file system contains the boot block (1kB)
	* contains the boot manager, which starts the operating systems
* Each block group contains a copy of the super block
	* Improves the data security
* The descriptor table contains among others:
	* The [[cluster]] numbers of the block bitmap and [[inode]] bitmap
	* The number of free [[clusters]] and inodes in the block group
* Block bitmap and [[inode]] bitmap are each a single [[cluster]] big
	* They contaion the information, which [[clusters]] and inodes in the block group a occupied
* The [[inode]] table contains the inodes of the block group
* The remaining [[clusters]] of the block group can be used for the data


#OPERATING_SYSTEM 
