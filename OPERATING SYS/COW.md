* Write operations do not modify/erase file system contents
	* Modified data is written into free clusters
	* Afterward, the metadata is modified for the new file
* Older file versions are preserved and can be restored
	* Data security is better compared with [journaling](Journal) file systems
	* Snapshots can be created without delay
#OPERATING_SYSTEM 