> operating system survive quite long in the industry

	The old stuff still in use bcs we can't get rid of that -> people upgrade that :V
> this shit is shit but still used bcs it's everywhere :V
# FAT 12
	Small scale limitation
* Num of [[cluster](cluster.md)]: 12 bits
	* up to 4096 = 2^12 [cluster](cluster.md)s can be addressed
* [cluster](cluster.md) size: 512 bytes to 4Kb
* Supports storage media up to 16Mb
>It is shit :v but this shit is in 1980 -> that is a lot
* File names are supported only in 8.3 format 
# FAT 16
* Release 1983 bcs ppl foresee that 16mb is not enough
* Up to 2^16 65524 [cluster](cluster.md)s can be addressed
* [cluster](cluster.md) size: 512 Bytes to 256kb
* File name are supported only in 8.3 format
* Main filed of application today: Mobile storage <= 2Gb
# FAT32
* Released in 1997 bcd the rising HDD capacities and bcs [cluster](cluster.md) >32kb waste a lot of storage
* Size of the [cluster](cluster.md) numbers records in the FAT: 32Bits
	* 4 Bits are reserved
	* -> 2^28 [cluster](cluster.md)s can be addressed
* [cluster](cluster.md) size = 512Bytes to 32kB
* Maximum file size: 4Gb
	* Reason: Only 4 Bytes are available for indication the file
* Main field of app today: Mobile storage media > 2Gb
# VFAT
* Virtual file allocation Table -> For long file name in 1997
	* Extension for FAT12/16/32 f
* support 4 the first time
	* names that do not comply with the 8,3 format
	* 255 char
* Sol
	* All special chars and dots inside the name are erased
	* All lowercase letters are converted to uppercase letters
	* Only the first 6 chars are kept
		* Next, a ~1 follows the dot
	* The first 3 char after the dot are kept and the rest is erased
	* If a file with the same name already exist :V add ~1, ~2
# exFAT (extended)
* in 2006
* up to 2^32 [cluster](cluster.md)s can be addressed
* [cluster](cluster.md) size: 512 Bytes to 64MB
* Max file size: 16 EB (2^64 byte)
* Main field of app: mobile *flash* memory
	* Fewer write operations than [[File Systems]] with a [[journal]] (NTFS -> slide 38)
#OPERATING_SYSTEM 