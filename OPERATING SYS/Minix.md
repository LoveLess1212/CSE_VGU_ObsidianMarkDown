* Standard Linus file system until 1992
	* Not surprising, because Minis was the basis of the development of Linux
* The Minix file system causes low [[overhead]]
	* Useful applications "today": Boot floppy disk and RAM disks
* Storage is represented as a linear chain of equal- sized blocks
* Aminix file system contains just 6 areas
	* Simple structure make it ideal for education purposes
## Boot block:
* contains the boot loader that starts the operating system
## Super block 
* Contain information about the file system
## Inodes bitmap: 
* Contain a list of all inodes with the information, whether the [[inode]] is occupied
## Inodes
* Contain the inodes with the [[OPERATING SYS/metadata]]
	* Every file and every directory is represented by at least a single [[inode]], which contains the [[OPERATING SYS/metadata]]
## Data
* Contains the contents of the files and directories
	* this is the biggest part in the file system
#OPERATING_SYSTEM 