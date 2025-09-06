# Problem:
## [[OPERATING SYS/metadata]] [[overhead]]
* Every [[inode]] at [[block addressing]] addresses a certain number of [[cluster]] numbers directly
* If a file requires more [[clusters]], they are indirectly addressed
* This addressing scheme causes rising [[overhead]] with rising file size
* -> Using extend :V
# Extent-based Addressing
* Unodes do not address individual [[clusters]], but instead create large areas of files to areas of contiguous blocks (extents) on the storage device
* Instead of many individual [[clusters]] numbers, only 3 values are required
	* Start ([[cluster]] number ) of area (extent) in the file
	* Size of the area in the file (in [[clusters]])
	* Number of the first [[cluster]] on the storage device
* Result: Lesser [[overhead]]
* Ex: JFS, XFS, btrfs, NTFS, ext4
# NTFS
* [[Cluster]] size: 512 Bytes to 64kB
* NTFS offers, compared with its predecessor [[FAT]], among others:
	* Maximum file size: 16TB
	* Maximum partition size: 256TB
	* Security features on file and directory level
* Equal to VFAT
	* implements NTFS file names up a length of 255 Unicode characters
	* implements NTFS interoperability with the MS-DOS operating system family by storing a unique file name in the format 8.3 for each file
## Structure of NTFS
* The file system contains a Master File Table
	* It contains the ref of the files to the [[cluster]]
	* Also contains the [[OPERATING SYS/metadata]] of the files
		* The content of small files <= 900 Bytes is stored directly in the MFT
* When a partition is formatted as, a fixed space is reserved for the MFT
	* 12.5% of the partition size is reserved for the MFT by default
	* If the MFT area has no more free capacity, the file system uses additional free space in the partition for the MFT
		* This may cause fragmentation of the MFT
![[Pasted image 20221205224359.png]]


#OPERATING_SYSTEM 