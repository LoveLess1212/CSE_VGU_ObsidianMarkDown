---
tags:
  - IT_SECURITY
---
1. What are the main tasks of an Operating system and how do they relate to security?
```
The main tasks of an operating system are: 
* working as Extended Machine
	* hides complicated detail from users and applications so that they don't have to deal with it
	* Provides Virtual Machine which is much easier to use
* working as Resource Manager
	* Allocates resources to different users
```
2. Explain how the access control mechanisms implemented by an Operating System can be circumvented by an attacker and in which case it can be enforced
```
- Access control mechanisms can be circumvented by an attacker by exploiting vulnerabilities in the system
- Access control mechanisms can be enforced by:
	- using a secure operating system
	- using a secure hardware
	- using a secure network
	- using a secure application
```
3. Explain Linux's access control mechanism in detail.
4. the ls-l command returns the following output:
```linux
drwxr-xr-x 2 max staff 4096 Mar 27 12:15 test
```
Explain each of the fields.
>[! Ans]
>ls -l return long listing information about the file/directory
>1st field: 
>	1st character: file type
>	2nd to 10th character: permission of owner -> group -> other, each 3 character represent read write execute permission
>2nd field: number of hard link
>3rd field: owner
>4th field: group
>5th field: size in byte
>6th field: last modified date ex: Mar 28 12:15
>7th field: name of file/directory 


```ans
* d: file type directory
* rwx(next 3 character): owner have permission to read,write and execute
* r-x(next 3 character): group only have permission to read and execute
* r-x(next 3 char): other only have permission to read and execute
* 2: number of hard link
* max: owner of the file-dir
* staff: group
* 4096: size of the file in byte
* Mar 27 12:15: last modified date
* test: name of the file/dir
```
5. Study the man pages for the commands 
- chmod
```
to change the permission of a file
chmod [OPTION] [MODE] [FILE_Name]
[OPTION]: 
- R: change the permission of the file recursively for all the file in the directory
- v: output a diagnostic for every file processed 
- c: like -v but report only when a change is made
[Mode]: class->operator->permission
	Class:
	- u: user/owner
	- g: group
	- o: other
	- a: all
	Operator:
	- +: add permission
	- -: remove permission
	- =: set permission
	Permission:
	- r: read
	- w: write
	- x: execute
```
- chown
```
- to change the owner(user or group) of a file
- chown [OPTION] [OWNER_name][:[GROUP_name]] FILE
ex: chown max:staff test.txt
the following command will change the owner of test.txt to max and the group to staff
ex2: chown :staff test.txt
the following command will change the group of test.txt to staff
```
- chgrp
```
- to change the group of a file
- chgrp [OPTION] GROUP FILE
ex: chgrp staff test.txt
the following command will change the group of test.txt to staff

```
For each command, give a brief summary of what it does and how it is used?
6. Consider the following file:
-rw-r--r-- 1 max staff 394 Apr 11 14:05 testfile.txt
How would the permissions of a unix file look after executing the following commands?
```
1. chmod go+w testfile.txt
-rw-rw-rw- 1 max staff 394 Apr 11 14:05 testfile.txt
2. chmod 123 testfile.txt
---x-w--wx 1 max staff 394 Apr 11 14:05 testfile.txt
```
7. 
	1. Which permissions are sufficient to execute a file containing a binary? Which permissions are sufficient toexecute a shell script?
	```
		To run a binary file, the user must only have execute permission on the file
		To run a shell script, the user must have both read and execute permission on the file
	```
	2. Which permissions are needed to copy a file?
	```
		To copy a file, the user must:
			have read and execute permission on the source directory 
			have read permission on the file
			have write and execute permission on the destination directory
		if the target file is not empty, the user must have write permission on the target file
	```
	3. Which permission are necessary to move a file?
	```
		to move a file, the user must:
			have write and execute permission on the source directory
			have read permission on the file if moving to different file system
			have write and execute permission on the destination directory
	```
8. What happen if you try the command ls -l as a user
	1. on a directory without having read-permissions?
		- ls: cannot open directory '.': Permission denied
	2. on a directory without having write-permissions?
		- list the content of the directory
	3. on a directory without having execute-permissions?
		- working normal
	4. Which permissions are sufficient necessary to change into an directory?
		- execute
9. Study the use of Access Control Lists under Linux and read the according man page. Explain what the commands
```
setfacl
- setfacl [OPTION] [ACL] FILE
	[OPTION]: 
		- -m: modify the ACL of the file
		- -x: remove the ACL of the file
		- -b: remove all the ACL of the file
		- -R: modify the ACL of the file recursively for all the file in the directory
		- -d: set the default ACL of the file
	[ACL]: [class]:[name]:[permission]
		- u: user - g: group - o: other - m: mask - d: default
		- r: read - w: write - x: execute
	ex. setfacl -m u:toan:rwx toan.txt
getfacl
	- getfacl [OPTION] FILE
	- getfacl return the ACL of the file
```
do and explain their practical use in a self-chosen example. What chances do the use of ACLs imply for the commands ls, cp and mv?
10. Consider the following directories:
``` 
drwxr-x--- 2 user1 groupa 4096 Apr 27 22:25 verzeichnisA/
- the folder verzeichnisA is owned by user1(read,write,execute) and groupa (read, execute)
drwxr-xr-- 2 user1 groupa 4096 Apr 27 22:26 verzeichnisB/
- the folder verzeichnisB is owned by user1(read,write,execute) and groupa (read)
drwxr-xrwx 2 user1 groupa 4096 Apr 27 22:26 verzeichnisC/
- the folder verzeichnisC is owned by user1(read,write,execute) and groupa (read, write, execute)
drwxrwxrwt 2 user1 groupa 4096 Apr 27 22:27 verzeichnisD/
- the folder verzeichnisD is owned by user1(read,write,execute) and groupa (read, write, execute)

where

ls -l verzeichnisA/
- the folder verzeichnisA is owned by user1(read,write,execute) and groupa (read, execute) others can't do anything with the folder
total 16
-rw-r--r-- 1 user1 groupa 2 Apr 27 22:23 dateiA1.txt
- the file dateiA1.txt is owned by user1(read,write) and groupa (read) -> user1 can read, write and execute the file, groupa (user1,user2) and others(user3) can only read the file
---------- 1 user1 groupa 2 Apr 27 22:24 dateiA2.txt
- the file dateiA2.txt is owned by user1(read,write) and groupa (read) -> user1, groupa (user1,user2) and others(user3) can't do anything with the file	
-rw------- 1 user1 groupa 2 Apr 27 22:24 dateiA3.txt
- the file dateiA3.txt is owned by user1(read,write) and groupa (read) -> user1 can read, write the file, groupa (user1,user2) and others(user3) can't do anything with the file
-r--r--r-- 1 user3 groupa 2 Apr 27 22:24 dateiA4.txt


ls -l verzeichnisB/
total 16
-rw-r--r-- 1 user1 groupa 2 Apr 27 22:26 dateiB5.txt
-rw---x--x 1 user1 groupa 2 Apr 27 22:25 dateiB6.txt
-rw-r--rw- 1 user1 groupa 2 Apr 27 22:26 dateiB7.txt
-rw------- 1 user1 groupa 2 Apr 27 22:26 dateiB8.txt

Consider user1, user2 belonging to groupa and user3 not belonging to groupa. For each
user, explain what happens when the following commands are issued and why:
```
• ls -l verzeichnisA 
• ls -l verzeichnisA/dateiA3.txt
• vi verzeichnisA/dateiA1.txt
• vi verzeichnisA/dateiA2.txt
• vi verzeichnisA/dateiA3.txt
• vi verzeichnisA/dateiA4.txt
• ls -l verzeichnisB
• ls -l verzeichnisB/dateiB6.txt
• vi verzeichnisB/dateiB5.txt
• vi verzeichnisB/dateiB6.txt
• vi verzeichnisB/dateiB7.txt
• vi verzeichnisB/dateiB8.txt
• rm verzeichnisC/dateiC9.txt
• rm verzeichnisC/dateiC11.txt
• cp verzeichnisC/dateiC10.txt verzeichnisD/dateiC10neu.txt
• mv verzeichnisC/dateiC10.txt verzeichnisD/dateiC10-1neu.txt
• cp verzeichnisC/dateiC12.txt verzeichnisD/dateiC12neu.txt
• mv verzeichnisC/dateiC12.txt verzeichnisD/dateiC12neu.txt
• touch verzeichnisC/dateiCNEU.txt
• cp verzeichnisD/dateiD13.txt verzeichnisD/dateiD13copy.txt
• rm verzeichnisD/dateiD14.txt
• rm verzeichnisD/dateiD15.txt
• vi verzeichnisD/dateiD16.txt
```