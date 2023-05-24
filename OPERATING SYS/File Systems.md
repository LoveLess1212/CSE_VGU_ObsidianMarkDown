# Purpose
* Organize the storage of files on data storage devices
	*  Files are sequences of Bytes of any length which belongs together with regard to content
* manage file names and attributes (metadata) of files
* form a namespace
	* Hierarchy of directories and files
> absolute path name: Name from the root to the file
> Relative path name: Name from the file to the destination
* **File system** are a Layer of the operating system
	* Processes and users access files via their abstract file names and not via their memory addresses
* **File system** should cause only little [[overhead]] for metadata
# Technical Principles
* Files systems address [[clusters]] and not blocks of the storage device
	* Each file occupies an integer number of [[clusters]]
* The size of the clusters is essential for the efficiency of the file system
	* The smaller the clusters are
		* Rising overhead for large files
		* Decreasing capacity loss due to internal fragmentation
	* The bigger the clusters are
		* Decreasing overhead for large files
		* Rising capacity loss due to internal fragmentation
	* The cluster size can be specified while creating the file system
# Linux File Systems
* The creation of a file causes the creation of an [[Inode]]
* *directory* is a file
	* content: file name and inode number for each file in the directory
* The traditional working method of Linux file systems: [[Block addressing]]

*absolute path names:* describe the complete path from the root to the file
*Relative path names:* All path, *do not begin with the root*
## [[FAT]]
## [[Journal]]

#OPERATING_SYSTEM 